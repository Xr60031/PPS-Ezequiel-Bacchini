from Funciones.Obtener_datos_facturacion.obtenedor_datos_facturacion import obtenedor_datos_facturacion
from Funciones.ID.obtenerdor_IDs import Obtenedor_ID
#NC = Nota de credito
class Obtenedor_NC(obtenedor_datos_facturacion):
    def __init__(self):
        super().__init__()

    def obtener_datos_facturacion(self, data_source, datos_factura_manager, datos_usuario):
        obtenedor_ID_nota_credito = Obtenedor_ID()
        datos_procesados, nro_cbte = datos_factura_manager.obtener_datos_nota_credito(data_source, datos_usuario)
        biblioteca_factura = self.armar_biblioteca_factura(datos_procesados)
        self.set_comprobante_anular(biblioteca_factura, biblioteca_factura['ID_factura_nota'])
        self.set_tipo_comprobante(biblioteca_factura, obtenedor_ID_nota_credito.obtener_ID_Nota(biblioteca_factura['tipo_factura_nota']), obtenedor_ID_nota_credito.obtener_Nombre_Nota(biblioteca_factura['tipo_factura_nota']))
        self.set_numero_comprobante(biblioteca_factura, nro_cbte)
        return biblioteca_factura