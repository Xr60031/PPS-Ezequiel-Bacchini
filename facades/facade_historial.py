from ExcelManager.historial_manager import obtener_historial

class Facade_Historial():
    def __init__(self):
        self

    def obtener_historial(self, path_excel):
        return obtener_historial(path_excel)