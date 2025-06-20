from Funciones.Obtener_datos_facturacion.obtenedor_datos_facturacion import obtenedor_datos_facturacion
#FM = Facturador Multiple
class Obtenedor_FM(obtenedor_datos_facturacion):
    def __init__(self):
        super().__init__()

    def obtener_datos_facturacion(self, data_source, datos_factura_manager, datos_usuario):
        bibliotecas_facturas = []
        biblioteca_datos = datos_factura_manager.obtener_datos_factura_multiple(data_source)
        for i in range(len(biblioteca_datos['datos_factura'])):
            datos = self.calcular_datos_items_tributos(biblioteca_datos[i]['items'], biblioteca_datos[i]['tributos'], biblioteca_datos[i]['datos_factura'], datos_usuario)
            bibliotecas_facturas.append(self.armar_biblioteca_factura(datos))
        return bibliotecas_facturas
