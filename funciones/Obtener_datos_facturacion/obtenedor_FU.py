from Funciones.Obtener_datos_facturacion.obtenedor_datos_facturacion import obtenedor_datos_facturacion

#FU = Facturador Unico
class Obtenedor_FU(obtenedor_datos_facturacion):
    def __init__(self):
        super().__init__()

    def obtener_datos_facturacion(self, data_source, datos_factura_manager, datos_usuario):
        datos_form = []
        items_formateados = []
        tributos_formateados = []
        datos_factura_manager.obtener_datos_factura_unica(data_source, datos_form, items_formateados, tributos_formateados)
        self.calcular_datos_items_tributos(items_formateados, tributos_formateados, datos_form, datos_usuario)
        biblioteca_factura = self.armar_biblioteca_factura(datos_form)

        return biblioteca_factura