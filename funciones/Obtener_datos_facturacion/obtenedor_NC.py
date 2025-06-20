from Funciones.Obtener_datos_facturacion.obtenedor_datos_facturacion import obtenedor_datos_facturacion
from Constantes import constantes_tipo_notas
#NC = Nota de credito
class Obtenedor_NC(obtenedor_datos_facturacion):
    def __init__(self):
        super().__init__()

    def obtener_datos_facturacion(self, data_source, datos_factura_manager, datos_usuario):
        datos_procesados, nro_cbte = datos_factura_manager.obtener_datos_nota_credito(data_source, datos_usuario)
        biblioteca_factura = self.armar_biblioteca_factura(datos_procesados)
        self.set_comprobante_anular(biblioteca_factura, biblioteca_factura['ID_factura_nota'])
        self.set_tipo_comprobante(biblioteca_factura, constantes_tipo_notas.tipo_nota_credito_c)
        self.set_numero_comprobante(biblioteca_factura, nro_cbte)
        print(biblioteca_factura)
        return biblioteca_factura