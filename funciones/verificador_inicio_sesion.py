def leer_llave(contenido_llave):
    return contenido_llave.startswith("-----BEGIN RSA PRIVATE KEY-----")

def leer_certificado(contenido_certificado):
    return contenido_certificado.startswith("-----BEGIN CERTIFICATE-----")