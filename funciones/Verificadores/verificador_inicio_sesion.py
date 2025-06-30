class Verificador_Inicio_Sesion():
    def __init__(self):
        self

    def leer_llave(self, contenido_llave):
        return contenido_llave.startswith("-----BEGIN RSA PRIVATE KEY-----")

    def leer_certificado(self, contenido_certificado):
        return contenido_certificado.startswith("-----BEGIN CERTIFICATE-----")