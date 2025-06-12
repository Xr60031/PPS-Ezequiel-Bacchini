from ExcelManager.item_manager import agregar_producto_servicio, modificar_producto_servicio, eliminar_producto_servicio, obtener_productos_servicios

class Facade_Items():
    def __init__(self):
        self

    def obtener_productos_servicios(self, destination_path):
        return obtener_productos_servicios(destination_path)

    def eliminar_producto_servicio(self, path_excel, nombre_item_target):
        return eliminar_producto_servicio(path_excel, nombre_item_target)

    def agregar_producto_servicio(self, path_excel, datos):
        return agregar_producto_servicio(path_excel, datos)

    def modificar_producto_servicio(self, path_excel, datos, nombre_item_target):
        return modificar_producto_servicio(path_excel, datos, nombre_item_target)