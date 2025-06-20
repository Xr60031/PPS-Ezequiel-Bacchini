def obtener_ID_tributo(impuesto):
    return{
        'Impuestos Nacionales' : 1,
        'Impuestos Provinciales' : 2,
        'Tributos Municipales' : 3,
        'Impuestos Internos' : 4,
        'IIBB' : 5,
        'Percepción de IVA' : 6,
        'Percepción de IIBB' : 7,
        'Percepciones por Tributos Municipales' : 8,
        'Otras Percepciones' : 9,
        'Percepción de IVA a no Categorizado' : 13,
        'Otros' : 99,
    }.get(impuesto)

def obtener_ID_documento(documento):
    return{
        'CONSUMIDOR FINAL' : 99,
        'CUIT' : 80,
        'CDI' : 87,
        'CI EXTRANJERA' : 91,
        'PASAPORTE' : 94,
        'DNI' : 96
    }.get(documento)

def obtener_ID_concepto(concepto):
    return{
        'PRODUCTOS' : 1,
        'SERVICIOS' : 2,
        'PRODUCTOS Y SERVICIOS' : 3
    }.get(concepto)

def obtener_ID_Factura(tipo_factura):
    return{
        'Factura C' : 11,
    }.get(tipo_factura)

def obtener_ID_condicion_iva_cliente(tipo_iva):
    return{
        'Consumidor Final': 5,
        'Monotributista' : 6,
        'Excento' : 4
    }.get(tipo_iva)