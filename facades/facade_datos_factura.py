from ExcelManager.obtener_datos_factura import obtener_datos_factura
from Funciones.formatear_datos_facturador_unico import formatear_items_, armar_datos_form, armar_diccionario_item
from Facades.facade_cleaner_hoja_facturacion import limpiar_hoja_facturacion
class Facade_datos_factura():
    def __init__(self):
        self
        
    def obtener_datos_factura_multiple(self, filename):
        datos_factura = obtener_datos_factura(filename)
        limpiar_hoja_facturacion(filename)
        return datos_factura
    
    def obtener_datos_factura_unica(self, data_source, datos_form, items_formateados, tributos_formateados):
        items_dict = armar_diccionario_item(data_source)
        armar_datos_form(datos_form, data_source)
        formatear_items_(items_dict, items_formateados, tributos_formateados)
        return