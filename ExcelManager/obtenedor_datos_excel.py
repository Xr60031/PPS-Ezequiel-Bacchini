class Obtenedor_Datos_Excel():
    def __init__(self):
        self

    def obtener_datos_hoja_factura_item_actual(self, factura_hoja, row):
        cantidad = float(factura_hoja.cell(row=row, column=14).value or 0)
        porcentaje_bonificado = factura_hoja.cell(row=row, column=13).value
        nombre_producto_servicio = factura_hoja.cell(row=row, column=12).value

        datos_hoja_factura = [
            int(cantidad),
            porcentaje_bonificado or 0,
            nombre_producto_servicio
        ]
        return datos_hoja_factura

    def obtener_datos_hoja_item_actual(self, items, datos_hoja_factura):
        row_ = 2
        while items.cell(row=row_, column=1).value and datos_hoja_factura[2] != items.cell(row=row_, column=1).value:
            row_ += 1

        codigo_producto = items.cell(row=row_, column=2).value
        descripcion = items.cell(row=row_, column=3).value
        precio_unitario = float(items.cell(row=row_, column=4).value or 0)
        impuesto_adicional = items.cell(row=row_, column=5).value
        descripcion_tributo_adicional = items.cell(row=row_, column=6).value
        alicuota = float(items.cell(row=row_, column=7).value or 0)
        
        importe_bonificado = 0
        subtotal = 0

        datos_hoja_item = [
            codigo_producto,
            descripcion,
            precio_unitario,
            impuesto_adicional,
            descripcion_tributo_adicional,
            alicuota,
            importe_bonificado,
            subtotal
        ]

        return datos_hoja_item