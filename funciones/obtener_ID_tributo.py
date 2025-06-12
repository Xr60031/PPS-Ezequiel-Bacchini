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