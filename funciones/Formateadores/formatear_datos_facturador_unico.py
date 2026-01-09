from Funciones.ID.obtenerdor_IDs import Obtenedor_ID 
import json as json_biblioteca

class Formateador_Datos_Facturador_Unico():
    def __init__(self):
        self

    def formatear_items_(self, items, items_formateados, tributos_formateados):
        obtenedor_id = Obtenedor_ID()
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

            id_tributo = obtenedor_id.obtener_ID_tributo(impuesto_adicional)
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
        

    def jsonify_items(self, data_source):
            items = data_source.form.getlist("selected_item")
            return [json_biblioteca.loads(p) for p in items]
        
    def armar_datos_form(self, datos_form, data_source):
        datos_form.append(data_source.form.get("id_factura"))
        datos_form.append(data_source.form.get("tipo_factura"))
        datos_form.append(data_source.form.get("tipo_doc"))
        datos_form.append(data_source.form.get("numero_doc_cliente"))
        datos_form.append(data_source.form.get("nombre_apellido_cliente"))
        datos_form.append(data_source.form.get("nro_telefono"))
        datos_form.append(data_source.form.get("provincia"))
        datos_form.append(data_source.form.get("localidad"))
        datos_form.append(data_source.form.get("domicilio"))
        datos_form.append(data_source.form.get("concepto_venta"))
        datos_form.append(data_source.form.get("concepto_iva"))
        datos_form.append(data_source.form.get("concepto"))
        datos_form.append(data_source.form.get("fecha_desde"))
        datos_form.append(data_source.form.get("fecha_hasta"))
        datos_form.append(data_source.form.get("fecha_vto_pago"))
