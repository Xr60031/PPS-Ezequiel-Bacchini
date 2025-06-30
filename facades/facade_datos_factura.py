from ExcelManager.obtener_datos_factura import Obtenedor_Datos_Factura
from Funciones.Formateadores.formatear_datos_facturador_unico import Formateador_Datos_Facturador_Unico
from Facades.facade_cleaner_hoja_facturacion import Cleaner_Facturacion_Hoja
from Funciones.Formateadores.formatear_datos_nota_credito import Formateador_Nota_Credito
from Funciones.obtenerdor_IDs import Obtenedor_ID
from Constantes import constantes_datos_FM, constantes_nota_credito

class Facade_datos_factura():
    def __init__(self):
        self
        
    def obtener_datos_factura_multiple(self, filename):
        obtenedor_datos_factura = Obtenedor_Datos_Factura()
        cleaner_excel = Cleaner_Facturacion_Hoja()
        datos_factura = obtenedor_datos_factura.obtener_datos_factura(filename)
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
        cleaner_excel.limpiar_hoja(filename)
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
        for datos in datos_listados:
            formateador_nota.transformar_a_tipos_correctos(datos)

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
                    obtenedor_ID.obtener_ID_tributo(lista[constantes_nota_credito.pos_impuesto_adicional]), # ID impuesto adicional 
                    lista[constantes_nota_credito.pos_descripcion_impuesto_adicional], # Descripcion 
                    lista[constantes_nota_credito.pos_subtotal], # Neto -> Subtotal
                    lista[constantes_nota_credito.pos_alicuota_impuesto_adicional], # Alicuota
                    lista[constantes_nota_credito.pos_subtotal] * lista[constantes_nota_credito.pos_alicuota_impuesto_adicional]/100 # Importe tributo -> Subtotal * Alicuota
                ])

        if datos_usuario['iag']:
            importe_neto = lista[constantes_nota_credito.pos_importe_neto]
            alicuota = datos_usuario['alicuota']
            tributos.append([
                datos_usuario['id_tributo_global'], # Id 
                datos_usuario['desc_iag'], # Descripcion
                importe_neto,  # IMPORTE NETO
                alicuota, # Alicuota
                importe_neto * alicuota / 100 # Importe Neto*Alicuota/100
            ])

        datos_factura.append(tributos)
        datos_factura.append(items)

        return datos_factura, numero_comprobante
        