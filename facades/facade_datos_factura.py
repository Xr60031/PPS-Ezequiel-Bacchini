from ExcelManager.obtener_datos_factura import obtener_datos_factura as obtener_datos_factura_multiple
from Funciones.Formateadores.formatear_datos_facturador_unico import formatear_items_, armar_datos_form, armar_diccionario_item
from Facades.facade_cleaner_hoja_facturacion import limpiar_hoja_facturacion
from Funciones.Formateadores.formatear_datos_nota_credito import transformar_a_lista,transformar_a_tipos_correctos, obtener_datos_factura as obtener_datos_nota
class Facade_datos_factura():
    def __init__(self):
        self
        
    def obtener_datos_factura_multiple(self, filename):
        datos_factura = obtener_datos_factura_multiple(filename)
        limpiar_hoja_facturacion(filename)
        return datos_factura
    
    def obtener_datos_factura_unica(self, data_source, datos_form, items_formateados, tributos_formateados):
        items_dict = armar_diccionario_item(data_source)
        armar_datos_form(datos_form, data_source)
        formatear_items_(items_dict, items_formateados, tributos_formateados)
        return
    
    def obtener_datos_nota_credito(self, data_source):
        datos_listados = transformar_a_lista(data_source)
        transformar_a_tipos_correctos(datos_listados)
        datos_factura = []
        obtener_datos_nota(datos_listados, datos_factura)
        return datos_listados
        