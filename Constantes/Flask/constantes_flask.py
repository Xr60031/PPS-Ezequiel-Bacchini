class constantes_de_flask:
    #Tiempo que tarda un archivo en eliminarse
    sleep_time = 2
    #Tiempo que tarda un archivo en eliminarse en un periodo extendido
    sleep_time_extended = 15

    #Posicion en el array de subida del excel al Drive
    embed = 1
    #Posicion en el array de subida del excel al Drive
    excel_id = 0 
    
    #Devuelve el nombre de la plantilla de Excel
    @staticmethod
    def excel_name(CUIT_Vendedor):
        return F'Plantilla_{CUIT_Vendedor}_.xlsx'
    #Modo para descargal Excel borrandolo del Drive
    excel_con_borrado_de_drive = 1
    #Modo para descargal Excel sin borrarlo del Drive
    excel_sin_borrado_de_drive = 0
    #Devuelve el path a donde se encuentra un archivo en las copias de plantilla
    @staticmethod
    def get_copy_path(output_file_name):
        return f'ExcelManager/Copies/{output_file_name}'
    #Devuelve el path de donde se encuentra la plantilla de Excel
    excel_template_path = 'ExcelManager/Plantilla/Plantilla_Factura.xlsx'
    #Devuelve el nombre del ZIP de facturación
    @staticmethod
    def zip_name(CUIT, FECHA, ACCION):
        return f"{ACCION}_{CUIT}_{FECHA}.zip"

    #Devuelve formateado el nombre del certificado
    @staticmethod
    def get_certificado_name(CUIT):
        return f"certificado_{CUIT}.crt"
    #Devuelve formateado el nombre de la llave
    @staticmethod
    def get_llave_privada_name(CUIT):
        return f"llave_privada_{CUIT}.key"
    #Devuelve la ruta de almacenamiento temporal del archivo pasado por parametro
    @staticmethod
    def get_upload_path(file_name):
        return f'uploads/{file_name}'

    #Devuelve el mensaje formateado para el manejo de Items
    @staticmethod
    def mensaje_accion_item(accion):
        return f"ITEM {accion} EXITOSAMENTE!"
    #Devuelve el mensaje de alerta de que al momento de intentar facturar, se detecto que faltaban datos
    factura_datos_faltantes_alerta = "Alerta: Faltan datos para poder realizar una factura"
    #Devuelve el mensaje de alerta de un archivo de excel no valido
    excel_no_valido_alerta = "Alerta: El archivo excel subido no es válido"
    #Devuelve el mensaje de alerta de que el CUIT ingresado no es válido
    cuit_no_valido_alerta = "Alerta: El CUIT ingresado no es válido"
    #Devuelve el mensaje de alerta de que no se generó la llave antes de intentar de generar el certificado
    llave_no_generada_alerta = "Alerta: La llave no fue generada, primero genere la llave"
    #Devuelve el mensaje de alerta de que la llave o el certificado no son validos
    llave_certificado_no_validos_alerta = "Alerta: La llave o el certificado no son válidos"
    #Devuelve el mensaje de alerta de que ocurrio un error
    algo_salio_mal_alerta = "Alerta: Algo salió mal"
    #Datos borrados exitosamente alerta
    datos_borrados_alerta = "Aviso: Los datos fueron borrados del sistema"
