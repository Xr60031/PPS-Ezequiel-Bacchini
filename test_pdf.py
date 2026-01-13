from impresor_pdf.impresor_pdf import Impresor_PDF

# =========================
# DATOS DE PRUEBA FACTURA
# =========================

datos_factura = {
    "Identificador_Factura": 2,
    "tipo_factura_nota": "Factura A",
    "Tipo_Documento": "CUIT",
    "Numero_de_documento_del_cliente": 20462668318,
    "Nombre_y_Apellido_Cliente": "Ezequiel Bacchini",
    "Telefono": "5491138857351",
    "Localidad": "Florida",
    "Provincia": "Buenos Aires",
    "Direccion": "Libertad 1971",
    "Condicion_de_venta_Cliente": "Contado",
    "Condicion_frente_al_IVA_Cliente": "Responsable Inscripto",
    "Concepto": "PRODUCTOS",

    "Fecha_servicio_desde": "",
    "Fecha_servicio_hasta": "",
    "Fecha_vencimiento_de_pago": "",

    "ID_doc": 80,
    "ID_concepto": 1,
    "ID_factura_nota": 1,
    "ID_IVA_cliente": 1,

    "Importe_Neto": 690.0,
    "Importe_Total": 795.0,
    "Importe_Tributo": 0.0,

    "Base_Imponible_sin_21%": 400.0,
    "Base_Imponible_sin_10.5%": 200.0,
    "Base_Imponible_0%": 90.0,
    "Importe_IVA_21%": 84.0,
    "Importe_IVA_10.5%": 21.0,

    "fecha_emision": "20260112",
    "nro_cbte_anular": None,
    "nro_cbte": None,
    "nro_CAE": None,
    "fecha_vto_CAE": None,

    # =========================
    # ITEMS
    # =========================
    "items": [
        ['Agua Mineral', 10, 1, '01', 'Agua mineral baja en sodio', 100.0, None, 0.0, 121.0, 21],
        ['Leche', 0, 1, '02', 'Leche Descremada', 200.0, 'Percepción de IVA', 0.0, 242.0, 10],
        ['Coca Cola Zero', 0, 1, '03', 'No contiene azucar', 400.0, 'Percepción de IVA', 0.0, 484.0, 99]
    ],

    # =========================
    # TRIBUTOS
    # =========================
    "tributos": [
        [6, 'Leche', 0, 10.5, 0, 'Leche'],
        [6, 'Gaseosa', 0, 21.0, 0, 'Coca Cola Zero']
    ]
}

# =========================
# DATOS VENDEDOR
# =========================

biblioteca_datos_vendedor = {
    "Nombre": "Carlos López",
    "CUIT": "20123456789",
    "Nombre_Empresa": "Tech Solutions",
    "Punto_de_venta": 1,
    "Razon_Social": "Tech Solutions SRL",
    "Domicilio": "Av. Siempre Viva 742, CABA",
    "Condicion_frente_al_IVA": "Responsable Monotributo",
    "Ingresos_Brutos": "Exento",
    "Fecha_Inicio": "2010-05-12"
}

# =========================
# DATOS CAE
# =========================

datos_CAE = [
    "73912345678901",  # CAE
    "2026-01-20",      # Fecha vto CAE
    2                  # Identificador factura
]

# =========================
# GENERAR PDF
# =========================

impresor = Impresor_PDF()
pdf_generado = impresor.generar_pdf_(datos_factura, biblioteca_datos_vendedor, datos_CAE)

with open("Factura_Test.pdf", "wb") as f:
    f.write(pdf_generado[1])

print("PDF generado correctamente: Factura_Test.pdf")
