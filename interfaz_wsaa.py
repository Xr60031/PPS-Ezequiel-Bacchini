import importlib
import datetime
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends.openssl.backend import backend
from cryptography.hazmat.primitives._serialization import PrivateFormat, NoEncryption, Encoding
from cryptography.x509.base import CertificateSigningRequestBuilder
from cryptography.x509.name import Name, NameOID, NameAttribute
from cryptography.hazmat.primitives.hashes import SHA256
#
from unicodedata import normalize
from warnings import warn
import shutil
import sys
#
from asn1crypto import cms, x509, pem
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
import base64
from cryptography.hazmat.primitives.asymmetric import padding
#
import os


wsaa_lib = importlib.import_module("PYAFIPWS.pyafipws-main.wsaa")

wsaa = wsaa_lib.WSAA()

def openssl_exe():
    try:
        openssl = shutil.which("openssl")
    except Exception:
        openssl = None
    if not openssl:
        if sys.platform.startswith("linux"):
            openssl = "openssl"
        else:
            if sys.maxsize <= 2 ** 32:
                openssl = r"c:\OpenSSL-Win32\bin\openssl.exe"
            else:
                openssl = r"c:\OpenSSL-Win64\bin\openssl.exe"
    return openssl

class InterfazWSAA():
    _public_methods_ = [
        "CrearPedidoCertificadoYLlavePrivada",
        "Crear_Llave_Privada",
        "Crear_Pedido_Certificado"
        "Crear_Ticket_Acceso_Firmado"

    ]

    _public_attrs_ = [
        "clave_privada",
        "pedido_cert",
        "bytesPedido",
        "bytesClave",
        "certificado",
        "TA",
        "RSA_key"
    ]

    def Crear_Llave_Privada(self, cuit, keyLength=2048):
        #Crea la llave privada

        ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        clave_privada = "clave_privada_%s_%s.key" % (cuit, ts)

        # create the RSA key pair (and save the result to a file):
        self.RSA_key = rsa.generate_private_key(
            0x10001, keyLength, backend
        )

        bytesClave = self.RSA_key.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm= NoEncryption(),
        )

        Clave = [bytesClave, clave_privada]
        
        self.bytesClave=bytesClave
        self.clave_privada=clave_privada

        return Clave

    def Crear_Pedido_Certificado (self, cuit , nombre, empresa):
        ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        pedido_cert = "pedido_cert_%s_%s.csr" % (cuit, ts)

        self.x509_req = CertificateSigningRequestBuilder()

        # normalizar encoding (reemplazar acentos, eñe, etc.)
        try:
            empresa = normalize("NFKD", empresa)
            nombre = normalize("NFKD", nombre)
        except TypeError as ex:
            # catch TypeError: normalize() argument 2 must be unicode, not str in python2
            warn(str(ex))

        # subjet: C=AR/O=[empresa]/CN=[nombre]/serialNumber=CUIT [nro_cuit]
        # sign the request with the previously created key (CrearClavePrivada)
        csrs = self.x509_req.subject_name(
            Name(
                [
                    NameAttribute(NameOID.COUNTRY_NAME, "AR"),
                    NameAttribute(NameOID.ORGANIZATION_NAME, "{}".format(empresa)),
                    NameAttribute(NameOID.COMMON_NAME, "{}".format(nombre)),
                    NameAttribute(NameOID.SERIAL_NUMBER, "CUIT {}".format(cuit)),
                ]
            )
        ).sign(self.RSA_key, SHA256(), backend)

        # save the CSR result to a file:
        bytesPedido=csrs.public_bytes(Encoding.PEM)

        self.pedido_cert=pedido_cert
        self.bytesPedido=bytesPedido

        pedido = [bytesPedido, pedido_cert]
        return pedido

    def CrearPedidoCertificadoYLlavePrivada(self, cuit , nombre, empresa, keyLength = 2048):
        ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        clave_privada = "clave_privada_%s_%s.key" % (cuit, ts)
        pedido_cert = "pedido_cert_%s_%s.csr" % (cuit, ts)

        # create the RSA key pair (and save the result to a file):
        rsa_key = rsa.generate_private_key(
            0x10001, keyLength, backend
        )

        bytesClave = rsa_key.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm= NoEncryption(),
        )

        with open(clave_privada, "wb") as archivo:
            archivo.write(bytesClave)

        self.x509_req = CertificateSigningRequestBuilder()

        # normalizar encoding (reemplazar acentos, eñe, etc.)
        try:
            empresa = normalize("NFKD", empresa)
            nombre = normalize("NFKD", nombre)
        except TypeError as ex:
            # catch TypeError: normalize() argument 2 must be unicode, not str in python2
            warn(str(ex))

        # subjet: C=AR/O=[empresa]/CN=[nombre]/serialNumber=CUIT [nro_cuit]
        # sign the request with the previously created key (CrearClavePrivada)
        csrs = self.x509_req.subject_name(
            Name(
                [
                    NameAttribute(NameOID.COUNTRY_NAME, "AR"),
                    NameAttribute(NameOID.ORGANIZATION_NAME, "{}".format(empresa)),
                    NameAttribute(NameOID.COMMON_NAME, "{}".format(nombre)),
                    NameAttribute(NameOID.SERIAL_NUMBER, "CUIT {}".format(cuit)),
                ]
            )
        ).sign(rsa_key, SHA256(), backend)

        # save the CSR result to a file:
        bytesPedido=csrs.public_bytes(Encoding.PEM)
        with open(pedido_cert, "wb") as f:
            f.write(bytesPedido)

        self.clave_privada=clave_privada
        self.pedido_cert=pedido_cert
        self.bytesClave=bytesClave
        self.bytesPedido=bytesPedido

    
    def sign_tra_for_afip(self, tra, cert_path, privatekey_path):
        # Leer y cargar la llave privada
        
        key_file=open(privatekey_path, "rb").read()

        private_key = serialization.load_pem_private_key(
            key_file,
            password=None,
            backend=default_backend()
        )

        # Leer y cargar el certificado
        cert_data= open(cert_path, "rb").read()
        
        if not cert_data.startswith(b"-----BEGIN CERTIFICATE-----"):
            raise ValueError("Certificado no válido")
        
        _, _, cert_data = pem.unarmor(cert_data)
        cert = x509.Certificate.load(cert_data)

        # Generar la firma digital del TRA
        signature = private_key.sign(
            data=bytes(tra, "utf-8"),
            padding=padding.PKCS1v15(),
            algorithm=hashes.SHA256()
        )

        issuer = cert.issuer
        serial_number = cert.serial_number

        # Crear la estructura PKCS#7
        signed_data = cms.SignedData({
            'version': 3,
            'digest_algorithms': [{'algorithm': 'sha256'}],
            'encap_content_info': {
                'content_type': 'data',
                'content': tra.encode('utf-8')  # Contenido firmado
            },
            'certificates': [cert],  # Incluir el certificado
            'signer_infos': [{
                'version': 3,
                'sid': cms.SignerIdentifier({
                    'issuer_and_serial_number': cms.IssuerAndSerialNumber({
                        'issuer': issuer,  # Usa el objeto convertido
                        'serial_number': serial_number
                    })
                }),
                'digest_algorithm': {'algorithm': 'sha256'},
                'signature_algorithm': {'algorithm': 'sha256_rsa'},
                'signature': signature
            }]
        })

        # Codificar en DER y luego en Base64
        content_info = cms.ContentInfo({
            'content_type': 'signed_data',
            'content': signed_data
        })
        der_encoded = content_info.dump()
        cms_base64 = base64.b64encode(der_encoded).decode('utf-8')

        return cms_base64

    def Crear_Ticket_Acceso_Firmado(self, service="wsfe", certificado="", clave="", cuit=""):
        if not os.path.exists(f"uploads\Ticket_Acceso{cuit}.xml"):
            print("Creando TRA...")
            tra = wsaa.CreateTRA(service, 2400) #Es la cantidad de segundos que va a ser válido el TICKET
            print("Firmando TRA...")
            cms = self.sign_tra_for_afip(tra=tra, cert_path=certificado, privatekey_path=clave)
            print("Conectando...")
            wsaa.Conectar(None, None, None, None, "CERTIFICADOS\cacert.pem", timeout=30*1*1)
            print("Iniciando CMS...")
            ta = wsaa.LoginCMS(cms)
            print("Creando Ticket de Acceso")
            with open(f"uploads/Ticket_Acceso{cuit}.xml", "w") as f:
                f.write(ta)
        else:
            ta = open(f"uploads/Ticket_Acceso{cuit}.xml").read()
        wsaa.AnalizarXml(xml=ta)
        wsaa.Token = wsaa.ObtenerTagXml("token")
        wsaa.Sign = wsaa.ObtenerTagXml("sign")

        return ta

if __name__ == '__main__':
    intWSAA = InterfazWSAA()
