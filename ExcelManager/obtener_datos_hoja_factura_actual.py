def obtener_datos_hoja_factura_item_actual(factura_hoja, row):
    cantidad = float(factura_hoja.cell(row=row, column=14).value or 0)
    porcentaje_bonificado = factura_hoja.cell(row=row, column=13).value
    nombre_producto_servicio = factura_hoja.cell(row=row, column=12).value

    datos_hoja_factura = [
        int(cantidad),
        porcentaje_bonificado or 0,
        nombre_producto_servicio
    ]
    return datos_hoja_factura