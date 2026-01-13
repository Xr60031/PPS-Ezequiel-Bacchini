from ExcelManager.obtener_datos_factura import Obtenedor_Datos_Factura
from Funciones.Formateadores.formatear_datos_facturador_unico import Formateador_Datos_Facturador_Unico
from Facades.Excel.facade_cleaner_hoja_facturacion import Cleaner_Facturacion_Hoja
from Funciones.Formateadores.formatear_datos_nota_credito import Formateador_Nota_Credito
from Funciones.ID.obtenerdor_IDs import Obtenedor_ID


from Constantes.Facturacion.constantes_items import constantes_posicion_items
from Constantes.Facturacion.constantes_arrays import constantes_array_datos_factura_FM
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
        obtenedor_ID = Obtenedor_ID()
        datos_listados = formateador_nota.transformar_a_lista(data_source)
        formateador_nota.transformar_a_tipos_correctos(datos_listados)

        numero_comprobante = datos_listados[constantes_historial.pos_Numero_Comprobante.value]

        datos_factura = []
        datos_factura += datos_listados[:constantes_historial.pos_Producto_Servicio.value]
        datos_factura += datos_listados[constantes_historial.pos_Importe_Neto.value:constantes_historial.pos_Descripcion_Impuesto_Adicional.value]

        items = []
        tributos = []

        i = 0
        item_actual = []
        for dato in range(constantes_historial.pos_Producto_Servicio.value, constantes_historial.pos_Importe_Neto.value):
            item_actual.append(datos_listados[dato])
            i+=1
        items.append(item_actual)

        if(datos_listados[constantes_historial.pos_Impuesto_Adicional.value]):
            tributos.append([
                obtenedor_ID.obtener_ID_tributo(datos_listados[constantes_historial.pos_Impuesto_Adicional.value]), # ID impuesto adicional 
                datos_listados[constantes_historial.pos_Descripcion_Impuesto_Adicional.value], # Descripcion 
                datos_listados[constantes_historial.pos_Subtotal.value], # Neto -> Subtotal
                datos_listados[constantes_historial.pos_Alicuota_Impuesto_Adicional.value], # Alicuota
                datos_listados[constantes_historial.pos_Subtotal.value] * datos_listados[constantes_historial.pos_Alicuota_Impuesto_Adicional.value]/100, # Importe tributo -> Subtotal * Alicuota
                item_actual[constantes_posicion_items.pos_producto_servicio.value] # Identificador que relaciona el tributo al producto correspondiente
            ])

        if datos_usuario['iag']:
            importe_neto = datos_listados[constantes_historial.pos_Importe_Neto.value]
            alicuota = datos_usuario['alicuota']
            tributos.append([
                datos_usuario['id_tributo_global'], # Id 
                datos_usuario['desc_iag'], # Descripcion
                importe_neto,  # IMPORTE NETO
                alicuota, # Alicuota
                importe_neto * alicuota / 100 # Importe Neto*Alicuota/100
            ])

        print("DATOS LISTADOS", datos_listados)

        datos_factura.append(tributos)
        datos_factura.append(items)
        datos_factura.append(datos_listados[constantes_historial.pos_base_21.value])
        datos_factura.append(datos_listados[constantes_historial.pos_base_105.value])
        datos_factura.append(datos_listados[constantes_historial.pos_base_0.value])
        datos_factura.append(datos_listados[constantes_historial.pos_Alicuota_21.value])
        datos_factura.append(datos_listados[constantes_historial.pos_Alicuota_10_5.value])

        return datos_factura, numero_comprobante
        