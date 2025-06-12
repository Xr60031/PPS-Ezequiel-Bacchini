def verificar_formateo_datos(datos_factura):
    datos_utilizables = False
    if(isinstance(datos_factura[0]["Identificador_Factura"], int)):
        ID = datos_factura[0]["Identificador_Factura"]
        ID_anterior = None
        datos_utilizables = True
        cant = len(datos_factura)
        i = 0
        while(i < cant and datos_utilizables != False):
            ID = datos_factura[0]["Identificador_Factura"]
            if(ID != ID_anterior):
                datos_utilizables = (
                    (isinstance(datos_factura[i]["Identificador_Factura"], int)) and
                    (isinstance(datos_factura[i]["tipo_factura_nota"], str)) and
                    (isinstance(datos_factura[i]["Nombre_y_Apellido_Cliente"], str)) and
                    (isinstance(datos_factura[i]["Tipo_Documento"], str)) and
                    (isinstance(datos_factura[i]["Numero_de_documento_del_cliente"], int)) and
                    (isinstance(datos_factura[i]["Condicion_de_venta_Cliente"], str)) and
                    (isinstance(datos_factura[i]["Condicion_frente_al_IVA_Cliente"], str)) and
                    (isinstance(datos_factura[i]["Concepto"], str)) and
                    (not datos_factura[i]["Fecha_servicio_desde"] or isinstance(datos_factura[i]["Fecha_servicio_desde"], str)) and
                    (not datos_factura[i]["Fecha_servicio_hasta"] or isinstance(datos_factura[i]["Fecha_servicio_hasta"], str)) and
                    (not datos_factura[i]["Fecha_vencimiento_de_pago"] or isinstance(datos_factura[i]["Fecha_vencimiento_de_pago"], str)) and
                    (isinstance(datos_factura[i]["ID_doc"], int)) and
                    (isinstance(datos_factura[i]["ID_concepto"], int)) and
                    (isinstance(datos_factura[i]["ID_factura_nota"], int)) and
                    (isinstance(datos_factura[i]["items"], list))
                )
            ID_anterior = ID
            i += 1

    return datos_utilizables
