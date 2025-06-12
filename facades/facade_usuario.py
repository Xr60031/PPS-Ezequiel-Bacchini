from ExcelManager.obtener_datos_usuario import obtener_datos_usuario
from Funciones.biblioteca_usuario import armar_biblioteca_vendedor

class Facade_usuario_manager():
    def __init__(self):
        self

    def armar_biblioteca_vendedor(self, datos_vendedor):
        return armar_biblioteca_vendedor(datos_vendedor)
    
    def obtener_datos_usuario(self, file_name):
        return obtener_datos_usuario(file_name)