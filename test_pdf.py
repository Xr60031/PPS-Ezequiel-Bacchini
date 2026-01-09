from impresor_pdf.impresor_pdf import Impresor_PDF

# Datos de prueba
datos_factura = {
    "Nombre_y_Apellido_Cliente": "Juan Pérez",
    "Importe_Total": 15200.75,
    "items": [
        ["Servicio de Hosting", "0%", "1", "H001", "Unidad", "12000.00", "ARS", "0.00", "12000.00", "21%", 12000*1.21],
        ["Dominio .com", "0%", "1", "D001", "Unidad", "2000.00", "ARS", "0.00", "2000.00", " ", 0],
        ["Soporte Técnico", "0%", "2", "S001", "Horas", "600.375", "ARS", "0.00", "1200.75", "21%", 600.375*1.21]
    ],
    "Condicion_de_venta_Cliente": "Contado",
    "Condicion_frente_al_IVA_Cliente": "Consumidor Final",
    "Fecha_vencimiento_de_pago": "2025-09-30",
    "Importe_Tributo": 0.01,
    "ID_factura_nota": 3,
    "Fecha_servicio_desde": "2025-09-01",
    "Fecha_servicio_hasta": "2025-09-30",
    "fecha_emision": "2025-08-25",
    "Tipo_Documento": 96,
    "Numero_de_documento_del_cliente": "32123456",

    "Telefono" : "+5491138857351",
    "Localidad": "Florida",
    "Provincia": "Buenos Aires",
    "Direccion": "Libertad 1781",
    "Importe_IVA_21%": 21,
    "Importe_IVA_10.5%" : 10.5,
}

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

datos_CAE = [
    "73912345678901",  # CAE
    "2025-09-10",      # Fecha de vencimiento del CAE
    12345              # Identificador de factura
]

impresor = Impresor_PDF()
pdf_generado = impresor.generar_pdf_(datos_factura, biblioteca_datos_vendedor, datos_CAE)

with open("Factura_Test.pdf", "wb") as f:
    f.write(pdf_generado[1])