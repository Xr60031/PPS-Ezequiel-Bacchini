import json as json_biblioteca

from Constantes.Facturacion.constantes_arrays import constantes_nota_credito


class Formateador_Nota_Credito():
    def __init__(self):
        self
    def transformar_a_lista(self, data_source):
            if data_source:
                return json_biblioteca.loads(data_source)
        
    def transformar_a_tipos_correctos(self, datos_factura):
        datos_factura[constantes_nota_credito.IDENTIFICADOR_FACTURA.value] = int(datos_factura[constantes_nota_credito.IDENTIFICADOR_FACTURA.value] or 0)
        datos_factura[constantes_nota_credito.TIPO_FACTURA_NOTA.value] = str(datos_factura[constantes_nota_credito.TIPO_FACTURA_NOTA.value] or "")
        datos_factura[constantes_nota_credito.TIPO_DE_DOCUMENTO.value] = str(datos_factura[constantes_nota_credito.TIPO_DE_DOCUMENTO.value] or "")
        datos_factura[constantes_nota_credito.NUMERO_DE_DOCUMENTO_CLIENTE.value] = int(datos_factura[constantes_nota_credito.NUMERO_DE_DOCUMENTO_CLIENTE.value] or 0)
        datos_factura[constantes_nota_credito.NOMBRE_Y_APELLIDO_CLIENTE.value] = str(datos_factura[constantes_nota_credito.NOMBRE_Y_APELLIDO_CLIENTE.value] or "")
        datos_factura[constantes_nota_credito.TELEFONO.value] = str(datos_factura[constantes_nota_credito.TELEFONO.value] or "")
        datos_factura[constantes_nota_credito.PROVINCIA.value] = str(datos_factura[constantes_nota_credito.PROVINCIA.value] or "")
        datos_factura[constantes_nota_credito.LOCALIDAD.value] = str(datos_factura[constantes_nota_credito.LOCALIDAD.value] or "")
        datos_factura[constantes_nota_credito.DOMICILIO.value] = str(datos_factura[constantes_nota_credito.DOMICILIO.value] or "")
        datos_factura[constantes_nota_credito.CONDICION_DE_VENTA_CLIENTE.value] = str(datos_factura[constantes_nota_credito.CONDICION_DE_VENTA_CLIENTE.value] or "")
        datos_factura[constantes_nota_credito.CONDICION_IVA_CLIENTE.value] = str(datos_factura[constantes_nota_credito.CONDICION_IVA_CLIENTE.value] or "")
        datos_factura[constantes_nota_credito.CONCEPTO.value] = str(datos_factura[constantes_nota_credito.CONCEPTO.value] or "")
        datos_factura[constantes_nota_credito.FECHA_SERVICIO_DESDE.value] = str(datos_factura[constantes_nota_credito.FECHA_SERVICIO_DESDE.value] or "")
        datos_factura[constantes_nota_credito.FECHA_SERVICIO_HASTA.value] = str(datos_factura[constantes_nota_credito.FECHA_SERVICIO_HASTA.value] or "")
        datos_factura[constantes_nota_credito.FECHA_VENCIMIENTO_DE_PAGO.value] = str(datos_factura[constantes_nota_credito.FECHA_VENCIMIENTO_DE_PAGO.value] or "")
        datos_factura[constantes_nota_credito.PRODUCTO_SERVICIO.value] = str(datos_factura[constantes_nota_credito.PRODUCTO_SERVICIO.value] or "")
        datos_factura[constantes_nota_credito.PORCENTAJE_BONIFICADO.value] = float(datos_factura[constantes_nota_credito.PORCENTAJE_BONIFICADO.value] or 0.0) 
        datos_factura[constantes_nota_credito.CANTIDAD.value] = int(datos_factura[constantes_nota_credito.CANTIDAD.value] or 0)
        datos_factura[constantes_nota_credito.CODIGO_PRODUCTO.value] = str(datos_factura[constantes_nota_credito.CODIGO_PRODUCTO.value] or "") 
        datos_factura[constantes_nota_credito.DESCRIPCION.value] = str(datos_factura[constantes_nota_credito.DESCRIPCION.value] or "")
        datos_factura[constantes_nota_credito.PRECIO_UNITARIO.value] = float(datos_factura[constantes_nota_credito.PRECIO_UNITARIO.value] or 0.0)
        datos_factura[constantes_nota_credito.IMPUESTO_ADICIONAL.value] = str(datos_factura[constantes_nota_credito.IMPUESTO_ADICIONAL.value] or "")
        datos_factura[constantes_nota_credito.IMPORTE_BONIFICADO.value] = float(datos_factura[constantes_nota_credito.IMPORTE_BONIFICADO.value] or 0.0)
        datos_factura[constantes_nota_credito.SUBTOTAL.value] = float(datos_factura[constantes_nota_credito.SUBTOTAL.value] or 0.0)
        datos_factura[constantes_nota_credito.IMPORTE_NETO.value] = float(datos_factura[constantes_nota_credito.IMPORTE_NETO.value] or 0.0)
        datos_factura[constantes_nota_credito.IMPORTE_TOTAL.value] = float(datos_factura[constantes_nota_credito.IMPORTE_TOTAL.value] or 0.0)
        datos_factura[constantes_nota_credito.IMPORTE_TRIBUTO.value] = float(datos_factura[constantes_nota_credito.IMPORTE_TRIBUTO.value] or 0.0)
        datos_factura[constantes_nota_credito.DESCRIPCION_IMPUESTO_ADICIONAL.value] = str(datos_factura[constantes_nota_credito.DESCRIPCION_IMPUESTO_ADICIONAL.value] or "")
        datos_factura[constantes_nota_credito.ALICUOTA_IMPUESTO_ADICIONAL.value] = int(datos_factura[constantes_nota_credito.ALICUOTA_IMPUESTO_ADICIONAL.value] or 0)
        datos_factura[constantes_nota_credito.NOMBRE_APELLIDO_VENDEDOR.value] = str(datos_factura[constantes_nota_credito.NOMBRE_APELLIDO_VENDEDOR.value] or "")
        datos_factura[constantes_nota_credito.CUIT_VENDEDOR.value] = int(datos_factura[constantes_nota_credito.CUIT_VENDEDOR.value] or 0)
        datos_factura[constantes_nota_credito.NOMBRE_EMPRESA.value] = str(datos_factura[constantes_nota_credito.NOMBRE_EMPRESA.value] or "")
        datos_factura[constantes_nota_credito.PUNTO_DE_VENTA.value] = int(datos_factura[constantes_nota_credito.PUNTO_DE_VENTA.value] or 0)
        datos_factura[constantes_nota_credito.RAZON_SOCIAL.value] = str(datos_factura[constantes_nota_credito.RAZON_SOCIAL.value] or "")
        datos_factura[constantes_nota_credito.DOMICILIO.value] = str(datos_factura[constantes_nota_credito.DOMICILIO.value] or "")
        datos_factura[constantes_nota_credito.CONDICION_FRENTE_AL_IVA.value] = str(datos_factura[constantes_nota_credito.CONDICION_FRENTE_AL_IVA.value] or "")
        datos_factura[constantes_nota_credito.INGRESOS_BRUTOS.value] = int(datos_factura[constantes_nota_credito.INGRESOS_BRUTOS.value] or 0)
        datos_factura[constantes_nota_credito.FECHA_INICIO.value] = str(datos_factura[constantes_nota_credito.FECHA_INICIO.value] or "")
        datos_factura[constantes_nota_credito.IMPUESTO_ADICIONAL_GLOBAL.value] = str(datos_factura[constantes_nota_credito.IMPUESTO_ADICIONAL_GLOBAL.value] or "")
        datos_factura[constantes_nota_credito.DESCRIPCION_IMPUESTO_ADICIONAL_GLOBAL.value] = str(datos_factura[constantes_nota_credito.DESCRIPCION_IMPUESTO_ADICIONAL_GLOBAL.value] or "")
        datos_factura[constantes_nota_credito.ALICUOTA_GLOBAL.value] = int(datos_factura[constantes_nota_credito.ALICUOTA_GLOBAL.value] or 0)
        datos_factura[constantes_nota_credito.CAE_NUMERO.value] = int(datos_factura[constantes_nota_credito.CAE_NUMERO.value] or 0)
        datos_factura[constantes_nota_credito.CAE_FECHA_VENCIMIENTO.value] = str(datos_factura[constantes_nota_credito.CAE_FECHA_VENCIMIENTO.value] or "")
        datos_factura[constantes_nota_credito.NUMERO_DE_COMPROBANTE.value] = int(datos_factura[constantes_nota_credito.NUMERO_DE_COMPROBANTE.value] or 0)

    def obtener_datos_factura(self, datos_form, datos_formateados):
        for i in range(constantes_nota_credito.IDENTIFICADOR_FACTURA.value, constantes_nota_credito.FECHA_VENCIMIENTO_DE_PAGO.value):
            datos_formateados.append(datos_form[i])