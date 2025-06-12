from Funciones.facturar import facturacion

class Facade_facturacion():
    def __init__(self):
        self
        
    def facturacion(self, destination_path, copy_path_llave, copy_path_certificado, datos_usuario, datos_factura, dataframe_historial):
        return facturacion(destination_path, copy_path_llave, copy_path_certificado, datos_usuario, datos_factura, dataframe_historial)