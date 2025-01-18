from pyafipws.wsfev1 import WSFEv1
from pyafipws.wsaa import WSAA
from datetime import datetime

# Configuración de conexión
cuit = 20462668318  # CUIT del contribuyente
cert_path = "PYAFIPWS\pyafipws-main\certificado.crt"  # Ruta a tu certificado
key_path = "PYAFIPWS\pyafipws-main\MiClavePrivada.key"  # Ruta a tu clave privada

# 1. Obtener el Ticket de Autorización WSAA
wsaa = WSAA(cuit=cuit, cert_path=cert_path, key_path=key_path)

# Solicitar el ticket de autenticación
wsaa_response = wsaa.CallWSAA()

wsaa.CrearPedidoCertificado()
wsaa.CrearClavePrivada()

if wsaa_response['errors']:
    print(f"Error al obtener el Ticket: {wsaa_response['errors']}")
else:
    # Ticket de autorización obtenido con éxito
    print(f"TICKET obtenido: {wsaa_response['ticket']}")

    # 2. Obtener el token para interactuar con el WSFE (Factura Electrónica)
    # Usamos el ticket de autorización obtenido para realizar operaciones con el WSFE
    wsfe = WSFEv1(cuit=cuit, ticket=wsaa_response['ticket'], cert_path=cert_path, key_path=key_path)

    # Definir los datos de la factura
    data = {
        'Concepto': 1,  # 1=Servicios, 2=Productos
        'PtoVta': 1,  # Punto de venta habilitado (ej. 1)
        'CbteTipo': 1,  # Tipo de comprobante (1=Factura A)
        'ImpTotal': 250.00,  # Total de la factura
        'ImpNeto': 200.00,  # Importe neto (sin IVA)
        'ImpIVA': 50.00,  # Importe IVA
        'DocTipo': 80,  # Tipo de documento del cliente (80=CUIT, 96=DNI, etc.)
        'DocNro': 20304050607,  # Número de documento del cliente (ej. CUIT cliente)
        'CbteDesde': 1,  # Número de comprobante desde
        'CbteHasta': 1,  # Número de comprobante hasta
        'CbteFch': datetime.today().strftime('%Y%m%d'),  # Fecha del comprobante (YYYYMMDD)
    }

    # Llamada al servicio para generar la factura electrónica
    response = wsfe.CrearFactura(data)

    # Manejo de la respuesta
    if response['errors']:
        print(f"Error al generar el comprobante: {response['errors']}")
    else:
        print(f"Comprobante generado con éxito. ID de comprobante: {response['cbte_id']}")