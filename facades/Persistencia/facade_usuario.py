from ExcelManager.usuario_manager import obtener_datos_usuario, armar_biblioteca_vendedor

class Facade_usuario_manager():
    def __init__(self):
        self

    def armar_biblioteca_vendedor(self, datos_vendedor):
        return armar_biblioteca_vendedor(datos_vendedor)
    
    def obtener_datos_usuario(self, file_name):
        return obtener_datos_usuario(file_name)