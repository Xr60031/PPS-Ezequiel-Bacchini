import json as json_biblioteca

from Constantes.Excel.constantes_excel import constantes_historial


class Formateador_Nota_Credito():
    def __init__(self):
        self
    def transformar_a_lista(self, data_source):
            if data_source:
                return json_biblioteca.loads(data_source)
        
    def transformar_a_tipos_correctos(self, datos_factura):
        datos_factura[constantes_historial.pos_Identificador_Factura.value-1] = int(datos_factura[constantes_historial.pos_Identificador_Factura.value-1] or 0)
        datos_factura[constantes_historial.pos_Tipo_Factura_Nota.value-1] = str(datos_factura[constantes_historial.pos_Tipo_Factura_Nota.value-1] or "")
        datos_factura[constantes_historial.pos_Tipo_Documento.value-1] = str(datos_factura[constantes_historial.pos_Tipo_Documento.value-1] or "")
        datos_factura[constantes_historial.pos_Numero_Documento_Cliente.value-1] = int(datos_factura[constantes_historial.pos_Numero_Documento_Cliente.value-1] or 0)
        datos_factura[constantes_historial.pos_Nombre_Apellido_Cliente.value-1] = str(datos_factura[constantes_historial.pos_Nombre_Apellido_Cliente.value-1] or "")
        datos_factura[constantes_historial.pos_Telefono.value-1] = str(datos_factura[constantes_historial.pos_Telefono.value-1] or "")
        datos_factura[constantes_historial.pos_Provincia.value-1] = str(datos_factura[constantes_historial.pos_Provincia.value-1] or "")
        datos_factura[constantes_historial.pos_Localidad.value-1] = str(datos_factura[constantes_historial.pos_Localidad.value-1] or "")
        datos_factura[constantes_historial.pos_Domicilio.value-1] = str(datos_factura[constantes_historial.pos_Domicilio.value-1] or "")
        datos_factura[constantes_historial.pos_Condicion_Venta_Cliente.value-1] = str(datos_factura[constantes_historial.pos_Condicion_Venta_Cliente.value-1] or "")
        datos_factura[constantes_historial.pos_Condicion_IVA_Cliente.value-1] = str(datos_factura[constantes_historial.pos_Condicion_IVA_Cliente.value-1] or "")
        datos_factura[constantes_historial.pos_Concepto.value-1] = str(datos_factura[constantes_historial.pos_Concepto.value-1] or "")
        datos_factura[constantes_historial.pos_Fecha_Servicio_Desde.value-1] = str(datos_factura[constantes_historial.pos_Fecha_Servicio_Desde.value-1] or "")
        datos_factura[constantes_historial.pos_Fecha_Servicio_Hasta.value-1] = str(datos_factura[constantes_historial.pos_Fecha_Servicio_Hasta.value-1] or "")
        datos_factura[constantes_historial.pos_Fecha_Vencimiento_Pago.value-1] = str(datos_factura[constantes_historial.pos_Fecha_Vencimiento_Pago.value-1] or "")
        datos_factura[constantes_historial.pos_Producto_Servicio.value-1] = str(datos_factura[constantes_historial.pos_Producto_Servicio.value-1] or "")
        datos_factura[constantes_historial.pos_Porcentaje_Bonificado.value-1] = float(datos_factura[constantes_historial.pos_Porcentaje_Bonificado.value-1] or 0.0) 
        datos_factura[constantes_historial.pos_Cantidad.value-1] = int(datos_factura[constantes_historial.pos_Cantidad.value-1] or 0)
        datos_factura[constantes_historial.pos_Codigo_Producto.value-1] = str(datos_factura[constantes_historial.pos_Codigo_Producto.value-1] or "") 
        datos_factura[constantes_historial.pos_Descripcion.value-1] = str(datos_factura[constantes_historial.pos_Descripcion.value-1] or "")
        datos_factura[constantes_historial.pos_Precio_Unitario.value-1] = float(datos_factura[constantes_historial.pos_Precio_Unitario.value-1] or 0.0)
        datos_factura[constantes_historial.pos_Impuesto_Adicional.value-1] = str(datos_factura[constantes_historial.pos_Impuesto_Adicional.value-1] or "")
        datos_factura[constantes_historial.pos_Importe_Bonificado.value-1] = float(datos_factura[constantes_historial.pos_Importe_Bonificado.value-1] or 0.0)
        datos_factura[constantes_historial.pos_Subtotal.value-1] = float(datos_factura[constantes_historial.pos_Subtotal.value-1] or 0.0)
        datos_factura[constantes_historial.pos_Importe_Neto.value-1] = float(datos_factura[constantes_historial.pos_Importe_Neto.value-1] or 0.0)
        datos_factura[constantes_historial.pos_Importe_Total.value-1] = float(datos_factura[constantes_historial.pos_Importe_Total.value-1] or 0.0)
        datos_factura[constantes_historial.pos_Importe_Tributo.value-1] = float(datos_factura[constantes_historial.pos_Importe_Tributo.value-1] or 0.0)
        datos_factura[constantes_historial.pos_Descripcion_Impuesto_Adicional.value-1] = str(datos_factura[constantes_historial.pos_Descripcion_Impuesto_Adicional.value-1] or "")
        datos_factura[constantes_historial.pos_Alicuota_Impuesto_Adicional.value-1] = int(datos_factura[constantes_historial.pos_Alicuota_Impuesto_Adicional.value-1] or 0)
        datos_factura[constantes_historial.pos_Nombre_Apellido_Vendedor.value-1] = str(datos_factura[constantes_historial.pos_Nombre_Apellido_Vendedor.value-1] or "")
        datos_factura[constantes_historial.pos_CUIT_Vendedor.value-1] = int(datos_factura[constantes_historial.pos_CUIT_Vendedor.value-1] or 0)
        datos_factura[constantes_historial.pos_Nombre_Empresa.value-1] = str(datos_factura[constantes_historial.pos_Nombre_Empresa.value-1] or "")
        datos_factura[constantes_historial.pos_Punto_Venta.value-1] = int(datos_factura[constantes_historial.pos_Punto_Venta.value-1] or 0)
        datos_factura[constantes_historial.pos_Razon_Social.value-1] = str(datos_factura[constantes_historial.pos_Razon_Social.value-1] or "")
        datos_factura[constantes_historial.pos_Domicilio.value-1] = str(datos_factura[constantes_historial.pos_Domicilio.value-1] or "")
        datos_factura[constantes_historial.pos_Condicion_Frente_IVA.value-1] = str(datos_factura[constantes_historial.pos_Condicion_Frente_IVA.value-1] or "")
        datos_factura[constantes_historial.pos_Ingresos_Brutos.value-1] = int(datos_factura[constantes_historial.pos_Ingresos_Brutos.value-1] or 0)
        datos_factura[constantes_historial.pos_Fecha_Inicio.value-1] = str(datos_factura[constantes_historial.pos_Fecha_Inicio.value-1] or "")
        datos_factura[constantes_historial.pos_Impuesto_Adicional_Global.value-1] = str(datos_factura[constantes_historial.pos_Impuesto_Adicional_Global.value-1] or "")
        datos_factura[constantes_historial.pos_Descripcion_Impuesto_Adicional_Global.value-1] = str(datos_factura[constantes_historial.pos_Descripcion_Impuesto_Adicional_Global.value-1] or "")
        datos_factura[constantes_historial.pos_Alicuota_Global.value-1] = int(datos_factura[constantes_historial.pos_Alicuota_Global.value-1] or 0)
        datos_factura[constantes_historial.pos_CAE_Numero.value-1] = int(datos_factura[constantes_historial.pos_CAE_Numero.value-1] or 0)
        datos_factura[constantes_historial.pos_CAE_Fecha_Vencimiento.value-1] = str(datos_factura[constantes_historial.pos_CAE_Fecha_Vencimiento.value-1] or "")
        datos_factura[constantes_historial.pos_Numero_Comprobante.value-1] = int(datos_factura[constantes_historial.pos_Numero_Comprobante.value-1] or 0)
        datos_factura[constantes_historial.pos_base_21.value-1] = int(datos_factura[constantes_historial.pos_base_21.value-1])
        datos_factura[constantes_historial.pos_base_105.value-1] = int(datos_factura[constantes_historial.pos_base_105.value-1])
        datos_factura[constantes_historial.pos_base_0.value-1] = int(datos_factura[constantes_historial.pos_base_0.value-1])
        datos_factura[constantes_historial.pos_Alicuota_21.value-1] = int(datos_factura[constantes_historial.pos_Alicuota_21.value-1] or 0)
        datos_factura[constantes_historial.pos_Alicuota_10_5.value-1] = int(datos_factura[constantes_historial.pos_Alicuota_10_5.value-1] or 0)

    def obtener_datos_factura(self, datos_form, datos_formateados):
        for i in range(constantes_historial.pos_Identificador_Factura.value-1, constantes_historial.pos_Fecha_Vencimiento_Pago.value-1):
            datos_formateados.append(datos_form[i])