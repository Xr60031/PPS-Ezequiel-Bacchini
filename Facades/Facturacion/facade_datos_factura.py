from ExcelManager.obtener_datos_factura import Obtenedor_Datos_Factura
from Funciones.Formateadores.formatear_datos_facturador_unico import Formateador_Datos_Facturador_Unico
from Facades.Excel.facade_cleaner_hoja_facturacion import Cleaner_Facturacion_Hoja
from Funciones.Formateadores.formatear_datos_nota_credito import Formateador_Nota_Credito

from Constantes.Facturacion.constantes_arrays import constantes_array_datos_factura_FM, constantes_data_source_NC
from Constantes.Excel.constantes_excel import constantes_historial

class Facade_datos_factura():
    def __init__(self):
        self
        
    def obtener_datos_factura_multiple(self, filename, worksheet):
        obtenedor_datos_factura = Obtenedor_Datos_Factura()
        cleaner_excel = Cleaner_Facturacion_Hoja()
        datos_factura = obtenedor_datos_factura.obtener_datos_factura(filename, worksheet)
        datos_procesados = []
        for factura_actual in datos_factura:
            items = factura_actual[constantes_array_datos_factura_FM.pos_items.value]
            tributos = factura_actual[constantes_array_datos_factura_FM.pos_tributos.value]
            del factura_actual [-1]
            del factura_actual [-1]
            datos_actual = {
                'datos_factura' : factura_actual,
                'items' : items,
                'tributos' : tributos 
            }
            datos_procesados.append(datos_actual)
        cleaner_excel.limpiar_hoja(filename, worksheet)
        return datos_procesados
    
    def obtener_datos_factura_unica(self, data_source):
        formateador_facturador_unico = Formateador_Datos_Facturador_Unico()
        items_formateados = []
        tributos_formateados = []
        datos_form = []
        items_dict = formateador_facturador_unico.jsonify_items(data_source)
        formateador_facturador_unico.armar_datos_form(datos_form, data_source)
        formateador_facturador_unico.formatear_items_(items_dict, items_formateados, tributos_formateados)
        datos = {
            'datos_factura' : datos_form,
            'items' : items_formateados,
            'tributos' : tributos_formateados
        }
        return datos
    
    def obtener_datos_nota_credito(self, data_source, datos_usuario):
        formateador_nota = Formateador_Nota_Credito()
        historial = data_source[constantes_data_source_NC.historial.value]
        fila_seleccionada = data_source[constantes_data_source_NC.fila_seleccionada.value]
        datos_procesados = []
        
        i=0
        while i<constantes_historial.pos_Fecha_Vencimiento_Pago.value:
            datos_procesados.append(fila_seleccionada[i])
            i+=1

        i=constantes_historial.pos_Importe_Neto.value-1
        while i<constantes_historial.pos_Importe_Tributo.value:
            datos_procesados.append(fila_seleccionada[i])
            i+=1

        tributos = formateador_nota.obtener_tributos_desde_historial(historial, datos_usuario, fila_seleccionada)
        datos_procesados.append(tributos)
        items = formateador_nota.transformar_items_a_lista(historial, fila_seleccionada)
        datos_procesados.append(items)

        i=constantes_historial.pos_base_21.value-1
        while i<constantes_historial.pos_Alicuota_10_5.value:
            datos_procesados.append(fila_seleccionada[i])
            i+=1

        formateador_nota.transformar_a_tipos_correctos(datos_procesados)
        numero_comprobante = fila_seleccionada[constantes_historial.pos_Numero_Comprobante.value]
        
        return datos_procesados, numero_comprobante
        