from Funciones.Obtener_datos_facturacion.obtenedor_datos_facturacion import obtenedor_datos_facturacion
from Constantes import constantes_dato_factura
#FM = Facturador Multiple
class Obtenedor_FM(obtenedor_datos_facturacion):
    def __init__(self):
        super().__init__()

    def obtener_datos_facturacion(self, data_source, datos_factura_manager, datos_usuario):
        bibliotecas_facturas = []
        datos_factura = datos_factura_manager.obtener_datos_factura_multiple(data_source)
        
        for i in range(len(datos_factura)):
            self.calcular_datos_items_tributos(datos_factura[i][constantes_dato_factura.pos_items], datos_factura[i][constantes_dato_factura.pos_tributos], datos_factura[i], datos_usuario)
            bibliotecas_facturas.append(self.armar_biblioteca_factura(datos_factura[i]))
        return bibliotecas_facturas
