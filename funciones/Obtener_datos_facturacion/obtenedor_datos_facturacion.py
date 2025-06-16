from abc import ABC, abstractmethod
from Funciones.obtenerdor_IDs import obtener_ID_concepto, obtener_ID_condicion_iva_cliente, obtener_ID_documento, obtener_ID_Factura
from datetime import datetime
from Constantes import constantes_items
from Constantes import constantes_dato_factura

class obtenedor_datos_facturacion(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def obtener_datos_facturacion(self, data_source, datos_factura_manager, datos_usuario):
        pass

    #Arma la biblioteca con los datos de la factura
    def armar_biblioteca_factura(self, datos_factura):
        datos_factura = {
            "Identificador_Factura": datos_factura[0],
            "tipo_factura_nota": datos_factura[1],
            "Nombre_y_Apellido_Cliente": datos_factura[2],
            "Tipo_Documento": datos_factura[3],
            "Numero_de_documento_del_cliente": int(datos_factura[4]),
            "Condicion_de_venta_Cliente": datos_factura[5],
            "Condicion_frente_al_IVA_Cliente": datos_factura[6],
            "Concepto": datos_factura[7],
            "Fecha_servicio_desde": datos_factura[8],
            "Fecha_servicio_hasta": datos_factura[9],
            "Fecha_vencimiento_de_pago": datos_factura[10],
            "ID_doc": obtener_ID_documento(datos_factura[3]),
            "ID_concepto": obtener_ID_concepto(datos_factura[7]),
            "ID_factura_nota": obtener_ID_Factura(datos_factura[1]),
            "ID_IVA_cliente": obtener_ID_condicion_iva_cliente(datos_factura[6]),
            "Importe_Neto": datos_factura[11],
            "Importe_Total": datos_factura[12],
            "Importe_Tributo": datos_factura[13],
            "tributos": datos_factura[14],
            "items": datos_factura[15],
            "nro_cbte_anular" : None,
            "fecha_emision" : datetime.now()
        }
        return datos_factura
    
    def calcular_datos_items_tributos(self, productos_servicios, tributos, datos_factura, biblioteca_datos_vendedor):
        imp_neto=0
        imp_total=0
        imp_total = float(imp_total)
        imp_tributo=0

        for i in range(len(productos_servicios)):
            importe_bonificado = productos_servicios[i][constantes_items.pos_cantidad]*productos_servicios[i][constantes_items.pos_precio_unitario]*(100-productos_servicios[i][constantes_items.pos_porcentaje_bonificado])/100
            alicuota = 0
            tributo_found = False
            j = 0
            while j < len(tributos) and tributo_found == False:
                if(tributos[j][constantes_items.pos_id_relacionado_tributo] == productos_servicios[i][constantes_items.pos_producto_servicio]):
                    alicuota = tributos[j][constantes_items.pos_alicuota_impuesto_adicional]
                    importe_tributo = importe_bonificado*alicuota/100 #imp tributo = importe bonificado*alicuota.
                    tributos[j][constantes_items.pos_importe_tributo] = importe_tributo
                    tributo_found = True
                j+=1
            subtotal = importe_bonificado*(100-alicuota)/100

            productos_servicios[i][constantes_items.pos_importe_bonificado] = importe_bonificado
            productos_servicios[i][constantes_items.pos_subtotal] = subtotal

            imp_total += subtotal
            imp_neto += importe_bonificado

        if biblioteca_datos_vendedor["id_tributo_global"]:
            tributos.append([
                #ID_tributo
                biblioteca_datos_vendedor["id_tributo_global"],
                #descripcion_impuesto_adicional
                biblioteca_datos_vendedor["desc_iag"],
                #imp_neto / importe bonificado
                imp_neto,
                #alicuota_impuesto_adicional
                biblioteca_datos_vendedor["alicuota"],
                #imp_neto*alicuota_impuesto_adicional
                imp_neto*(biblioteca_datos_vendedor["alicuota"] or 0)/100,
                None #No está relacionada con ningún producto particular
            ])
            imp_total += imp_neto*(biblioteca_datos_vendedor["alicuota"] or 0)/100

        datos_factura.append(imp_neto)
        datos_factura.append(imp_total)

        #Este es el importe tributo total
        if len(tributos) == 0:
            datos_factura.append(0)
        else:
            imp_tributo = imp_total - imp_neto
            datos_factura.append(imp_tributo)
        
        datos_factura.append(tributos)
        datos_factura.append(productos_servicios)

    def set_comprobante_anular(datos_factura, cbte_anular):
        datos_factura["nro_cbte_anular"] = cbte_anular