from Funciones.Obtener_datos_facturacion.obtenedor_datos_facturacion import obtenedor_datos_facturacion

#NC = Nota de credito
class Obtenedor_NC(obtenedor_datos_facturacion):
    def __init__(self):
        super().__init__()

    def obtener_datos_facturacion(self, data_source, datos_factura_manager, datos_usuario):
        datos_listados = datos_factura_manager.obtener_datos_nota_credito(data_source)
        biblioteca_factura = self.armar_biblioteca_factura(datos_listados)
        return biblioteca_factura