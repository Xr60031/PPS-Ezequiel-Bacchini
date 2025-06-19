from Funciones.obtenerdor_IDs import obtener_ID_tributo
def armar_datos_producto_servicio(productos_servicios, tributos, datos_hoja_factura, datos_hoja_item):
    productos_y_servicios_actual = [
        datos_hoja_factura[2],  # 0 - Producto/Servicio
        datos_hoja_factura[1],  # 1 - Porcentaje Bonificado
        datos_hoja_factura[0],  # 2 - Cantidad
        datos_hoja_item[0],  # 3 - Código Producto
        datos_hoja_item[1],  # 4 - Descripción
        datos_hoja_item[2],  # 5 - Precio Unitario
        datos_hoja_item[3],  # 6 - Impuesto Adicional
        datos_hoja_item[6],  # 7- Importe Bonificado
        datos_hoja_item[7],# 8- Subtotal
    ] 

    productos_servicios.append(productos_y_servicios_actual)

    id_tributo = obtener_ID_tributo(datos_hoja_item[3])
    if(id_tributo):

        tributos_actual = [
            id_tributo, # 0 - ID_tributo
            datos_hoja_item[4], # 1 - descripcion_impuesto_adicional
            datos_hoja_item[6], # 2 -Importe Bonificado
            datos_hoja_item[5], # 3 - alicuota_impuesto_adicional
            0, # 4 - Importe tributo
            datos_hoja_factura[2] # 5 -ID_relacionada_a_producto
        ]
        tributos.append(tributos_actual)

    return