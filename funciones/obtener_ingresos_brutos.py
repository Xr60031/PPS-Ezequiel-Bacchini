from pyafipws.padron import WSConsultaPadron

# Configuración
CUIT_EMISOR = 20345678901  # Tu CUIT

# Archivos necesarios
cert_path = "mi_certificado.crt"
key_path = "mi_clave.key"
ta_path = "token-padron.xml"

# Inicializar conexión
ws = WSConsultaPadron(cert_path, key_path, ta_path, cache=False)
ws.Cuit = CUIT_EMISOR
ws.Conectar()  # Esto genera el TA si es necesario

# Consultar el padrón
data = ws.Consultar(CUIT_EMISOR)

if data["resultado"] == "A":
    # Obtener el número de Ingresos Brutos
    ingresos_brutos = data["datos"].get("ingresos_brutos", "No disponible")
    print(f"Número de Ingresos Brutos: {ingresos_brutos}")
else:
    print("❌ Error:", data.get("errmsg", "Consulta rechazada"))
