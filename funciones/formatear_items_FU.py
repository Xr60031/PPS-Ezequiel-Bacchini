from funciones.obtener_ID_tributo import obtener_ID_tributo

def formatear_items_facturador_unico(items, items_formateados, tributos_formateados):
    i=0
    while i < len(items):
        cantidad = int(items[i]["cantidad"])
        precio_unitario = float(items[i]["precio_unitario"])
        porcentaje_bonificado = items[i]["porcentaje_bonificado"]
        impuesto_adicional = items[i]["impuesto_adicional"]
        importe_bonificado = cantidad*precio_unitario*(100-porcentaje_bonificado)/100
        alicuota = float(items[i]["alicuota"] or 0) 

        producto_actual = [
            items[i]["nombre"], # Producto/Servicio
            porcentaje_bonificado, # Porcentaje Bonificado
            cantidad, # Cantidad
            items[i]["codigo"], # Código Producto
            items[i]["descripcion_producto"], # Descripción
            precio_unitario, # Precio Unitario
            impuesto_adicional, # Impuesto Adicional
            importe_bonificado, # Importe Bonificado
            importe_bonificado*(100-alicuota)/100 # Subtotal
        ]
        items_formateados.append(producto_actual)

        id_tributo = obtener_ID_tributo(impuesto_adicional)
        if(id_tributo):

            tributo_actual = [
                id_tributo, #ID_tributo
                items[i]["descripcion_impuesto_adicional"], #descripcion_impuesto_adicional
                importe_bonificado, #Precio_Bonificado 
                alicuota, #alicuota_impuesto_adicional
                importe_bonificado*alicuota#Precio_Bonificado*alicuota_impuesto_adicional
            ]
            tributos_formateados.append(tributo_actual)
        
        i += 1

def agregar_items_tributos_resultados(items, tributos, biblioteca_factura, biblioteca_datos_vendedor):
    imp_total = 0
    imp_neto = 0
    i = 0
    while i < len(items):
        # + subtotal
        imp_total += items[i][8]
        # + importe_bonificado
        imp_neto += items[i][7]
        i += 1

    if biblioteca_datos_vendedor["id_tributo_global"]:
        tributos.append([
            #ID_tributo
            biblioteca_datos_vendedor["id_tributo_global"],
            #descripcion_impuesto_adicional
            biblioteca_datos_vendedor["desc_iag"],
            #imp_neto
            imp_neto,
            #alicuota_impuesto_adicional
            biblioteca_datos_vendedor["alicuota"],
            #imp_neto*alicuota_impuesto_adicional
            imp_neto*(biblioteca_datos_vendedor["alicuota"] or 0)/100
        ])
        imp_total += imp_neto*(biblioteca_datos_vendedor["alicuota"] or 0)/100

    biblioteca_factura["tributos"] = tributos
    if len(biblioteca_factura["tributos"]) == 0:
        biblioteca_factura["Importe_Tributo"] = 0
    else:
        imp_tributo = imp_total - imp_neto
        biblioteca_factura["Importe_Tributo"] = imp_tributo

    biblioteca_factura["Importe_Total"] = imp_total
    biblioteca_factura["Importe_Neto"] = imp_neto
    biblioteca_factura["tributos"] = tributos
    biblioteca_factura["items"] = items
    
    
    