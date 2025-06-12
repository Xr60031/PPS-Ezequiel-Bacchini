from ExcelManager.dataframes_manager import obtener_dataframe_facturar, obtener_dataframe_historial, obtener_xml, guardar_xml

class Facade_dataframe():
    def __init__(self):
        self

    def obtener_dataframe_historial(self, file_name):
        return obtener_dataframe_historial(file_name)
    
    def obtener_dataframe_facturar(self, file_name):
        return obtener_dataframe_facturar(file_name)
    
    def obtener_xml(self, file_name):
        return obtener_xml(file_name)
    
    def guardar_xml(self, filename, xml):
        guardar_xml(filename, xml)
    
