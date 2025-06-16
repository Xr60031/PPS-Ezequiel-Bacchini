from Funciones.Obtener_datos_facturacion.obtenedor_datos_facturacion import obtenedor_datos_facturacion
import json as json_biblioteca

#NC = Nota de credito
class Obtenedor_NC(obtenedor_datos_facturacion):
    def __init__(self):
        super().__init__()

    def transformar_a_lista(self, data_source):
        if data_source:
            return json_biblioteca.loads(data_source)
        
        for i in range(0, 11):
            return    
        
    def obtener_productos_tributos(self, datos_form, items, tributos):
        for i in range(len(datos_form)):

            item_actual = []
        for dato in range(11,20):
            item_actual.append(datos_form[i][dato])

        items.append(item_actual)

        tributos_actual = []
        tributos_actual.append(datos_form[i][19])
        tributos_actual.append(datos_form[i][25])
        tributos_actual.append(datos_form[i][26])
        tributos_actual.append(datos_form[i][27])
        tributos_actual.append(datos_form[i][20])

        tributos.append(tributos_actual)

    def obtener_datos_factura(self, datos_form, datos_formateados):
        for i in range(0, 11):
            datos_formateados.append(datos_form[0][i])

        for i in range(26, 40):
            datos_formateados.append(datos_form[0][i])

    def obtener_datos_facturacion(self, data_source, datos_factura_manager, datos_usuario):
        datos_listados = self.transformar_a_lista(data_source)
        
        items_formateados = []
        tributos_formateados = []
        self.obtener_productos_tributos(datos_listados, items_formateados, tributos_formateados)
        print("-"*25)
        print(datos_listados)
        print("-"*25)
        print(items_formateados)
        print("-"*25)
        print(tributos_formateados)
        print("-"*25)
        datos_formateados = []
        self.obtener_datos_factura(datos_listados, datos_formateados)
        print(datos_formateados)

        datos_formateados = self.armar_biblioteca_factura(datos_formateados)
        agregar_items_tributos_resultados(items_formateados, tributos_formateados, datos_formateados, datos_usuario)
        datos_factura = []
        datos_factura.append(datos_formateados)
        return datos_factura