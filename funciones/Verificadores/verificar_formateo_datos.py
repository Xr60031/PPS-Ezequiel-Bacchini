
class Verificador_Formateo_Datos_Facturacion():
    def __init__(self):
        self

    def verificar_formateo_datos(self, datos_factura):
        return(
            isinstance(datos_factura["Identificador_Factura"],int) and
            isinstance(datos_factura["tipo_factura_nota"],str) and
            isinstance(datos_factura["Tipo_Documento"],str) and
            isinstance(datos_factura["Numero_de_documento_del_cliente"],int) and
            isinstance(datos_factura["Nombre_y_Apellido_Cliente"],str) and
            isinstance(datos_factura["Telefono"],(str, int)) and
            isinstance(datos_factura["Localidad"],str) and
            isinstance(datos_factura["Provincia"],str) and
            isinstance(datos_factura["Direccion"],str) and
            isinstance(datos_factura["Condicion_de_venta_Cliente"],str) and
            isinstance(datos_factura["Condicion_frente_al_IVA_Cliente"],str) and
            isinstance(datos_factura["Concepto"],str) and
            isinstance(datos_factura["Fecha_servicio_desde"],(str, type(None))) and
            isinstance(datos_factura["Fecha_servicio_hasta"],(str, type(None))) and
            isinstance(datos_factura["Fecha_vencimiento_de_pago"],(str, type(None))) and
            isinstance(datos_factura["ID_doc"],(int, type(None))) and
            isinstance(datos_factura["ID_concepto"],int) and
            isinstance(datos_factura["ID_factura_nota"],int) and
            isinstance(datos_factura["ID_IVA_cliente"],int) and
            isinstance(datos_factura["Importe_Neto"], (float, type(None))) and
            isinstance(datos_factura["Importe_Total"], (float, type(None))) and
            isinstance(datos_factura["Importe_Tributo"], (float, type(None))) and
            isinstance(datos_factura["tributos"], (list, type(None))) and
            isinstance(datos_factura["items"], list,) and
            isinstance(datos_factura["nro_cbte_anular"], (int, type(None))) and
            isinstance(datos_factura["fecha_emision"], str)
        )