from Funciones.obtenerdor_IDs import obtener_ID_tributo
import json as json_biblioteca

def formatear_items_(items, items_formateados, tributos_formateados):
    i=0
    while i < len(items):
        cantidad = int(items[i]["cantidad"])
        precio_unitario = float(items[i]["precio_unitario"])
        porcentaje_bonificado = items[i]["porcentaje_bonificado"]
        impuesto_adicional = items[i]["impuesto_adicional"]
        alicuota = float(items[i]["alicuota"] or 0) 
        importe_bonificado = 0
        subtotal = 0

        producto_actual = [
            items[i]["nombre"], # 0 Producto/Servicio
            porcentaje_bonificado, # 1 Porcentaje Bonificado
            cantidad, # 2 Cantidad
            items[i]["codigo"], # 3 Código Producto
            items[i]["descripcion_producto"], # 4 Descripción
            precio_unitario, # 5 Precio Unitario
            impuesto_adicional, # 6 Impuesto Adicional
            importe_bonificado, # 7 Importe Bonificado
            subtotal # 8 Subtotal
        ]
        items_formateados.append(producto_actual)

        id_tributo = obtener_ID_tributo(impuesto_adicional)
        if(id_tributo):

            tributo_actual = [
                id_tributo, #ID_tributo
                items[i]["descripcion_impuesto_adicional"], #descripcion_impuesto_adicional
                importe_bonificado, #importe bonificado
                alicuota, #alicuota_impuesto_adicional
                0, #importe tributo = Precio_Bonificado*alicuota_impuesto_adicional
                producto_actual[0] #ID_producto relacionado
            ]
            tributos_formateados.append(tributo_actual)
        
        i += 1
    

def armar_diccionario_item(data_source):
        items = data_source.form.getlist("selected_item")
        return [json_biblioteca.loads(p) for p in items]
    
def armar_datos_form(datos_form, data_source):
    datos_form.append(data_source.form.get("id_factura"))# 0
    datos_form.append(data_source.form.get("tipo_factura"))# 1
    datos_form.append(data_source.form.get("nombre_apellido_cliente"))# 2
    datos_form.append(data_source.form.get("tipo_doc"))# 3
    datos_form.append(data_source.form.get("numero_doc_cliente"))# 4
    datos_form.append(data_source.form.get("concepto_venta"))# 5
    datos_form.append(data_source.form.get("concepto_iva"))# 6
    datos_form.append(data_source.form.get("concepto"))# 7
    datos_form.append(data_source.form.get("fecha_desde"))# 8
    datos_form.append(data_source.form.get("fecha_hasta"))# 9
    datos_form.append(data_source.form.get("fecha_vto_pago"))# 10
