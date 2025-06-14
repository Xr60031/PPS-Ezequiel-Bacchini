from abc import ABC, abstractmethod

class obtenedor_datos_facturacion(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def obtener_datos_facturacion(self, data_source, datos_factura_manager, datos_usuario):
        pass