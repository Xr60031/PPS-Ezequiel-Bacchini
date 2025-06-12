from Funciones.obtenerdor_IDs import obtener_ID_tributo
def armar_datos_producto_servicio(productos_servicios, tributos, datos_hoja_factura, datos_hoja_item):
    productos_y_servicios_actual = [
        datos_hoja_factura[2],  # Producto/Servicio
        datos_hoja_factura[1],  # Porcentaje Bonificado
        datos_hoja_factura[0],  # Cantidad
        datos_hoja_item[0],  # Código Producto
        datos_hoja_item[1],  # Descripción
        datos_hoja_item[2],  # Precio Unitario
        datos_hoja_item[3],  # Impuesto Adicional
        datos_hoja_item[6],  # Importe Bonificado
        datos_hoja_item[7]# Subtotal
    ] 

    productos_servicios.append(productos_y_servicios_actual)

    id_tributo = obtener_ID_tributo(datos_hoja_item[3])
    if(id_tributo):

        tributos_actual = [
            id_tributo, #ID_tributo
            datos_hoja_item[4], #descripcion_impuesto_adicional
            datos_hoja_item[6], #Precio_Bonificado 
            datos_hoja_item[5], #alicuota_impuesto_adicional
            datos_hoja_item[6]*datos_hoja_item[5]#Precio_Bonificado*alicuota_impuesto_adicional
        ]
        tributos.append(tributos_actual)

    return