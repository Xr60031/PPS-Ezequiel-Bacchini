from ExcelManager.obtener_datos_factura import obtener_datos_factura
from Funciones.biblioteca_factura import armar_biblioteca_factura
class Facade_datos_factura():
    def __init__(self):
        self

    def armar_biblioteca_factura(self, datos_factura_):
        return armar_biblioteca_factura(datos_factura_)
    
    def obtener_datos_factura(self, filename, biblioteca_datos_vendedor):
        return obtener_datos_factura(filename, biblioteca_datos_vendedor)