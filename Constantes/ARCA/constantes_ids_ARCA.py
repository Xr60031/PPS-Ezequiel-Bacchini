from enum import Enum

# IDs de tributos
class ID_Tributo(Enum):
    IMPUESTOS_NACIONALES = 1
    IMPUESTOS_PROVINCIALES = 2
    TRIBUTOS_MUNICIPALES = 3
    IMPUESTOS_INTERNOS = 4
    IIBB = 5
    PERCEPCION_DE_IVA = 6
    PERCEPCION_DE_IIBB = 7
    PERCEPCIONES_POR_TRIBUTOS_MUNICIPALES = 8
    OTRAS_PERCEPCIONES = 9
    PERCEPCION_DE_IVA_NO_CATEGORIZADO = 13
    OTROS = 99

# IDs de tipo de documento
class ID_Documento(Enum):
    CONSUMIDOR_FINAL = 99
    CUIT = 80
    CDI = 87
    CI_EXTRANJERA = 91
    PASAPORTE = 94
    DNI = 96

# IDs de concepto
class ID_Concepto(Enum):
    PRODUCTOS = 1
    SERVICIOS = 2
    PRODUCTOS_Y_SERVICIOS = 3

# IDs de tipo de factura
class ID_Factura(Enum):
    FACTURA_C = 11
    FACTURA_A = 1
    FACTURA_B = 6

# IDs de tipo de nota de crédito
class ID_Nota_Credito(Enum):
    NOTA_C = 13
    NOTA_A = 3
    NOTA_B = 8
    NOTA_C_Nombre = "NOTA CREDITO C"
    NOTA_A_Nombre = "NOTA CREDITO A"
    NOTA_B_Nombre = "NOTA CREDITO B"

# IDs de condición IVA cliente
class ID_Condicion_IVA_Cliente(Enum):
    CONSUMIDOR_FINAL = 5
    MONOTRIBUTISTA = 6
    EXCENTO = 4
    RESPONSABLE_INSCRIPTO = 1