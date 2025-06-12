from ExcelManager.config_manager import guardar_configuracion_inicial, guardar_configuracion

class Facade_Configuracion():
    def __init__(self):
        self
    
    def guardar_configuracion_inicial(self, template_path,config,copy_path):
        return guardar_configuracion_inicial(template_path,config,copy_path)
    
    def guardar_configuracion(self, path_excel, config):
        return guardar_configuracion(path_excel, config)