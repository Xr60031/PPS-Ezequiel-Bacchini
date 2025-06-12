def leer_llave(contenido_llave: str) -> bool:
    return contenido_llave.startswith("-----BEGIN RSA PRIVATE KEY-----")

def validar_llave(contenido_llave: str):
    global llave_aprobada
    llave_aprobada = leer_llave(contenido_llave)

def leer_certificado(contenido_certificado: str) -> bool:
    return contenido_certificado.startswith("-----BEGIN CERTIFICATE-----")

def validar_certificado(contenido_certificado: str):
    global certificado_aprobado
    certificado_aprobado = leer_certificado(contenido_certificado)
