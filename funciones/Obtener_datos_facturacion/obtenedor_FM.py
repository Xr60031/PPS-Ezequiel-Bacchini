from Funciones.Obtener_datos_facturacion.obtenedor_datos_facturacion import obtenedor_datos_facturacion
from Facades.facade_cleaner_hoja_facturacion import limpiar_hoja_facturacion

class Obtenedor_FM(obtenedor_datos_facturacion):
    def __init__(self):
        super().__init__()

    def obtener_datos_facturacion(self, data_source, datos_factura_manager, datos_usuario):
        datos_factura = datos_factura_manager.obtener_datos_factura(data_source, datos_usuario)
        limpiar_hoja_facturacion(data_source)
        return datos_factura
