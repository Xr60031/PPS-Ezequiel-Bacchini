from ExcelManager.obtener_datos_factura import obtener_datos_factura as obtener_datos_factura_multiple
from Funciones.Formateadores.formatear_datos_facturador_unico import formatear_items_, armar_datos_form, jsonify_items
from Facades.facade_cleaner_hoja_facturacion import limpiar_hoja_facturacion
from Funciones.Formateadores.formatear_datos_nota_credito import transformar_a_lista,transformar_a_tipos_correctos, obtener_datos_factura as obtener_datos_nota
from Funciones.obtenerdor_IDs import obtener_ID_tributo
from Constantes import constantes_datos_FM, constantes_nota_credito
class Facade_datos_factura():
    def __init__(self):
        self
        
    def obtener_datos_factura_multiple(self, filename):
        datos_factura = obtener_datos_factura_multiple(filename)
        datos_procesados = []
        for factura_actual in datos_factura:
            items = factura_actual[constantes_datos_FM.pos_items]
            tributos = factura_actual[constantes_datos_FM.pos_tributos]
            del factura_actual [-1]
            del factura_actual [-1]
            datos_actual = {
                'datos_factura' : factura_actual,
                'items' : items,
                'tributos' : tributos 
            }
            datos_procesados.append(datos_actual)
        limpiar_hoja_facturacion(filename)
        return datos_procesados
    
    def obtener_datos_factura_unica(self, data_source):
        items_formateados = []
        tributos_formateados = []
        datos_form = []
        items_dict = jsonify_items(data_source)
        armar_datos_form(datos_form, data_source)
        formatear_items_(items_dict, items_formateados, tributos_formateados)
        datos = {
            'datos_factura' : datos_form,
            'items' : items_formateados,
            'tributos' : tributos_formateados
        }
        return datos
    
    def obtener_datos_nota_credito(self, data_source, datos_usuario):
        datos_listados = transformar_a_lista(data_source)
        for datos in datos_listados:
            transformar_a_tipos_correctos(datos)

        numero_comprobante = datos_listados[0][constantes_nota_credito.pos_numero_comprobante]

        datos_factura = []
        datos_factura += datos_listados[0][:constantes_nota_credito.pos_producto_servicio]
        datos_factura += datos_listados[0][constantes_nota_credito.pos_importe_neto:constantes_nota_credito.pos_descripcion_impuesto_adicional]

        items = []
        tributos = []

        for lista in datos_listados:
            i = 0
            items_actual = []
            for dato in range(constantes_nota_credito.pos_producto_servicio, constantes_nota_credito.pos_importe_neto):
                items_actual.append(lista[dato])
                i+=1
            items.append(items_actual)

            if(lista[constantes_nota_credito.pos_impuesto_adicional]):
                tributos.append([
                    obtener_ID_tributo(lista[constantes_nota_credito.pos_impuesto_adicional]), # ID impuesto adicional 
                    lista[constantes_nota_credito.pos_descripcion_impuesto_adicional], # Descripcion 
                    lista[constantes_nota_credito.pos_subtotal], # Neto -> Subtotal
                    lista[constantes_nota_credito.pos_alicuota_impuesto_adicional], # Alicuota
                    lista[constantes_nota_credito.pos_subtotal] * lista[constantes_nota_credito.pos_alicuota_impuesto_adicional]/100 # Importe tributo -> Subtotal * Alicuota
                ])

        if datos_usuario['iag']:
            pass

        datos_factura.append(tributos)
        datos_factura.append(items)

        return datos_factura, numero_comprobante
        