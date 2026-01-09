from abc import ABC, abstractmethod
from Funciones.ID.obtenerdor_IDs import Obtenedor_ID
from datetime import datetime

from Constantes.Facturacion.constantes_items import constantes_posicion_items, constantes_posicion_tributos
from Constantes.Facturacion.constantes_arrays import constantes_factura

class obtenedor_datos_facturacion(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def obtener_datos_facturacion(self, data_source, datos_factura_manager, datos_usuario):
        pass

    def truncar_a_dos_decimales(self, valor):
        return int(valor * 100) / 100

    #Arma la biblioteca con los datos de la factura
    def armar_biblioteca_factura(self, datos_factura):
        obtenedor_id = Obtenedor_ID()
        datos_factura = {
            "Identificador_Factura": int(datos_factura[constantes_factura.identificador_factura.value]),
            "tipo_factura_nota": datos_factura[constantes_factura.tipo_factura_nota.value],
            "Tipo_Documento": datos_factura[constantes_factura.tipo_documento.value],
            "Numero_de_documento_del_cliente": int(datos_factura[constantes_factura.numero_de_documento_del_cliente.value] or 0),
            "Nombre_y_Apellido_Cliente": datos_factura[constantes_factura.nombre_y_apellido_cliente.value],
            "Telefono" : datos_factura[constantes_factura.telefono.value],
            "Localidad": datos_factura[constantes_factura.localidad.value],
            "Provincia": datos_factura[constantes_factura.provincia.value],
            "Direccion": datos_factura[constantes_factura.domicilio.value],
            "Condicion_de_venta_Cliente": datos_factura[constantes_factura.condicion_de_venta_cliente.value],
            "Condicion_frente_al_IVA_Cliente": datos_factura[constantes_factura.condicion_frente_al_iva_cliente.value],
            "Concepto": datos_factura[constantes_factura.concepto.value],
            "Fecha_servicio_desde": datos_factura[constantes_factura.fecha_servicio_desde.value].strftime('%Y%m%d') if hasattr(datos_factura[constantes_factura.fecha_servicio_desde.value], 'strftime') else datos_factura[constantes_factura.fecha_servicio_desde.value],
            "Fecha_servicio_hasta": datos_factura[constantes_factura.fecha_servicio_hasta.value].strftime('%Y%m%d') if hasattr(datos_factura[constantes_factura.fecha_servicio_hasta.value], 'strftime') else datos_factura[constantes_factura.fecha_servicio_hasta.value],
            "Fecha_vencimiento_de_pago": datos_factura[constantes_factura.fecha_vencimiento_de_pago.value].strftime('%Y%m%d') if hasattr(datos_factura[constantes_factura.fecha_vencimiento_de_pago.value], 'strftime') else datos_factura[constantes_factura.fecha_vencimiento_de_pago.value],
            "ID_doc": obtenedor_id.obtener_ID_documento(datos_factura[constantes_factura.tipo_documento.value]),
            "ID_concepto": obtenedor_id.obtener_ID_concepto(datos_factura[constantes_factura.concepto.value]),
            "ID_factura_nota": obtenedor_id.obtener_ID_Factura(datos_factura[constantes_factura.tipo_factura_nota.value]),
            "ID_IVA_cliente": obtenedor_id.obtener_ID_condicion_iva_cliente(datos_factura[constantes_factura.condicion_frente_al_iva_cliente.value]),
            "Importe_Neto": self.truncar_a_dos_decimales(datos_factura[constantes_factura.importe_neto.value]),
            "Importe_Total": self.truncar_a_dos_decimales(datos_factura[constantes_factura.importe_total.value]),
            "Importe_Tributo": self.truncar_a_dos_decimales(datos_factura[constantes_factura.importe_tributo.value]),
            "tributos": datos_factura[constantes_factura.tributos.value],
            "items": datos_factura[constantes_factura.items.value],
            "nro_cbte_anular" : None,
            "nro_cbte": None,
            "fecha_emision" : datetime.now().strftime('%Y%m%d'),
            "nro_CAE": None,
            "fecha_vto_CAE": None,
            "Base_Imponible_sin_21%": constantes_factura.base_imponible_sin_21.value,
            "Base_Imponible_sin_10.5%": constantes_factura.base_imponible_sin_105.value,
            "Importe_IVA_21%": constantes_factura.importe_iva_21.value,
            "Importe_IVA_10.5%": constantes_factura.importe_iva_105.value,
        }
        return datos_factura
    
    def calcular_datos_items_tributos(self, productos_servicios, tributos, datos_factura, biblioteca_datos_vendedor):
        imp_neto=0.0
        imp_total=0.0
        imp_tributo_total=0.0
        base_imponible_sin_21 = 0
        importe_iva_21 = 0
        base_imponible_sin_105 = 0
        importe_iva_105 = 0

        for item in productos_servicios:
            neto = item[constantes_posicion_items.pos_cantidad.value]*item[constantes_posicion_items.pos_precio_unitario.value]
            importe_bonificado = neto * (item[constantes_posicion_items.pos_porcentaje_bonificado.value])/100
            subtotal = neto - importe_bonificado
            alicuota = 0
            tributo_found = False
            j = 0
            while j < len(tributos) and tributo_found == False:
                if(tributos[j][constantes_posicion_tributos.pos_id_relacionado_tributo.value] == item[constantes_posicion_items.pos_producto_servicio.value]):
                    alicuota = tributos[j][constantes_posicion_tributos.pos_alicuota_impuesto_adicional.value]
                    imp_tributo = subtotal*alicuota/100
                    ### AGREGADO PARA EL IVA
                    if alicuota == 21:
                        base_imponible_sin_21 += subtotal
                        importe_iva_21 += subtotal*alicuota/100
                    elif alicuota == 10.5 :
                        base_imponible_sin_105 += subtotal
                        importe_iva_105 += subtotal*alicuota/100
                    ###
                    imp_tributo_total += imp_tributo
                    tributos[j][constantes_posicion_tributos.pos_importe_tributo.value] = imp_tributo
                    tributo_found = True
                j+=1

            item[constantes_posicion_items.pos_importe_bonificado.value] = importe_bonificado
            item[constantes_posicion_items.pos_subtotal.value] = subtotal

            imp_neto += subtotal

        if biblioteca_datos_vendedor["id_tributo_global"]:
            tributos.append([
                #ID_tributo
                biblioteca_datos_vendedor["id_tributo_global"],
                #descripcion_impuesto_adicional
                biblioteca_datos_vendedor["desc_iag"],
                #imp_neto
                imp_neto,
                #alicuota_impuesto_adicional
                biblioteca_datos_vendedor["alicuota"],
                #imp_neto*alicuota_impuesto_adicional -> Es el importe tributo
                imp_neto*(biblioteca_datos_vendedor["alicuota"] or 0)/100,
                None #No está relacionada con ningún producto particular
            ])
            imp_tributo_total += imp_neto*(biblioteca_datos_vendedor["alicuota"] or 0)/100

        imp_total = imp_neto + imp_tributo_total

        datos_calculados = []
        datos_calculados += datos_factura
        datos_calculados.append(imp_neto)
        datos_calculados.append(imp_total)
        datos_calculados.append(imp_tributo_total)
        datos_calculados.append(tributos)
        datos_calculados.append(productos_servicios)
        datos_calculados.append(base_imponible_sin_21)
        datos_calculados.append(importe_iva_21)
        datos_calculados.append(base_imponible_sin_105)
        datos_calculados.append(importe_iva_105)
        
        return datos_calculados

    def set_comprobante_anular(self, datos_factura, cbte_anular):
        datos_factura["nro_cbte_anular"] = cbte_anular

    def set_tipo_comprobante(self, datos_factura, tipo_cbte, nota_credito):
        datos_factura["ID_factura_nota"] = tipo_cbte
        datos_factura["tipo_factura_nota"] = nota_credito

    def set_numero_comprobante(self, datos_factura, nro_cbte):
        datos_factura["nro_cbte"] = nro_cbte