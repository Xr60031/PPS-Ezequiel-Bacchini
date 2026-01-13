from Funciones.ID.obtenerdor_IDs import Obtenedor_ID
from Constantes.Excel.constantes_excel import constantes_historial
from Constantes.Facturacion.constantes_arrays import constantes_array_biblioteca_factura


class Formateador_Nota_Credito():
    def __init__(self):
        self

    def avanzar_fila(self, numero_fila_actual):
        numero_fila_actual+=1
        return numero_fila_actual

    def transformar_items_a_lista(self, historial, fila_seleccionada):
        items = []

        start_index = fila_seleccionada[constantes_historial.pos_Identificador_Factura.value-1]
        fila_id_buscado = start_index

        numero_fila_actual = 0
        fila_actual_id = historial[numero_fila_actual][constantes_historial.pos_Identificador_Factura.value-1]

        while fila_actual_id != fila_id_buscado:
            numero_fila_actual = self.avanzar_fila(numero_fila_actual)
            fila_actual_id = historial[numero_fila_actual][constantes_historial.pos_Identificador_Factura.value-1]
        
        fila= historial[numero_fila_actual]
        item_actual = [
            fila[constantes_historial.pos_Producto_Servicio.value-1],  # Producto/Servicio
            fila[constantes_historial.pos_Porcentaje_Bonificado.value-1],  # Porcentaje Bonificado
            fila[constantes_historial.pos_Cantidad.value-1],  # Cantidad
            fila[constantes_historial.pos_Codigo_Producto.value-1],  # Codigo Producto
            fila[constantes_historial.pos_Descripcion.value-1],  # Descripcion
            fila[constantes_historial.pos_Precio_Unitario.value-1],  # Precio unitario
            fila[constantes_historial.pos_Impuesto_Adicional.value-1],  # Impuesto Adicional
            fila[constantes_historial.pos_Importe_Bonificado.value-1],  # Importe Bonificado
            fila[constantes_historial.pos_Subtotal.value-1],  # Subtotal
            fila[constantes_historial.pos_Alicuota_Impuesto_Adicional.value-1],  # Alicuota

        ]

        numero_fila_actual = self.avanzar_fila(numero_fila_actual)
        fila_actual_id = historial[numero_fila_actual][constantes_historial.pos_Identificador_Factura.value-1]
        items.append(item_actual)
        fila= historial[numero_fila_actual]

        while fila_actual_id is None:
            item_actual = [
                fila[constantes_historial.pos_Producto_Servicio.value-1],  # Producto/Servicio
                fila[constantes_historial.pos_Porcentaje_Bonificado.value-1],  # Porcentaje Bonificado
                fila[constantes_historial.pos_Cantidad.value-1],  # Cantidad
                fila[constantes_historial.pos_Codigo_Producto.value-1],  # Codigo Producto
                fila[constantes_historial.pos_Descripcion.value-1],  # Descripcion
                fila[constantes_historial.pos_Precio_Unitario.value-1],  # Precio unitario
                fila[constantes_historial.pos_Impuesto_Adicional.value-1],  # Impuesto Adicional
                fila[constantes_historial.pos_Importe_Bonificado.value-1],  # Importe Bonificado
                fila[constantes_historial.pos_Subtotal.value-1],  # Subtotal
                fila[constantes_historial.pos_Alicuota_Impuesto_Adicional.value-1],  # Alicuota
            ]
            numero_fila_actual = self.avanzar_fila(numero_fila_actual)
            fila_actual_id = historial[numero_fila_actual][constantes_historial.pos_Identificador_Factura.value-1]
            items.append(item_actual)
            fila= historial[numero_fila_actual]

        return items
        
    def obtener_tributos_desde_historial(self, historial, datos_usuario, fila_seleccionada):
        obtenedor_ID = Obtenedor_ID()
        tributos = []

        start_index = fila_seleccionada[constantes_historial.pos_Identificador_Factura.value-1]
        fila_id_buscado = start_index

        numero_fila_actual = 0
        fila_actual_id = historial[numero_fila_actual][constantes_historial.pos_Identificador_Factura.value-1]

        imp_neto_total = 0.0

        while fila_actual_id != fila_id_buscado:
            numero_fila_actual = self.avanzar_fila(numero_fila_actual)
            fila_actual_id = historial[numero_fila_actual][constantes_historial.pos_Identificador_Factura.value-1]

        fila = historial[numero_fila_actual]

        impuesto_adicional = fila[constantes_historial.pos_Impuesto_Adicional.value-1] or None
        descripcion_impuesto = fila[constantes_historial.pos_Descripcion_Impuesto_Adicional.value-1]
        alicuota = float(fila[constantes_historial.pos_Alicuota_Impuesto_Adicional.value-1] or 0)
        subtotal = float(fila[constantes_historial.pos_Subtotal.value-1] or 0)
        producto_servicio = fila[constantes_historial.pos_Producto_Servicio.value-1]

        imp_neto_total += subtotal

        if impuesto_adicional and alicuota not in (0, 10.5, 21):
            id_tributo = obtenedor_ID.obtener_ID_tributo(impuesto_adicional)
            importe_tributo = subtotal * alicuota / 100

            tributo_actual = [
                id_tributo,
                descripcion_impuesto,
                subtotal,
                alicuota,
                importe_tributo,
                producto_servicio
            ]
            tributos.append(tributo_actual)

        numero_fila_actual = self.avanzar_fila(numero_fila_actual)
        fila_actual_id = historial[numero_fila_actual][constantes_historial.pos_Identificador_Factura.value-1]
        fila = historial[numero_fila_actual]

        while fila_actual_id is None:
            impuesto_adicional = fila[constantes_historial.pos_Impuesto_Adicional.value-1] or None
            descripcion_impuesto = fila[constantes_historial.pos_Descripcion_Impuesto_Adicional.value-1]
            alicuota = float(fila[constantes_historial.pos_Alicuota_Impuesto_Adicional.value-1] or 0)
            subtotal = float(fila[constantes_historial.pos_Subtotal.value-1] or 0)
            producto_servicio = fila[constantes_historial.pos_Producto_Servicio.value-1]

            imp_neto_total += subtotal

            if impuesto_adicional and alicuota not in (0, 10.5, 21):
                id_tributo = obtenedor_ID.obtener_ID_tributo(impuesto_adicional)
                importe_tributo = subtotal * alicuota / 100

                tributo_actual = [
                    id_tributo,
                    descripcion_impuesto,
                    subtotal,
                    alicuota,
                    importe_tributo,
                    producto_servicio
                ]
                tributos.append(tributo_actual)

            fila_actual_id = historial[numero_fila_actual][constantes_historial.pos_Identificador_Factura.value-1]
            numero_fila_actual = self.avanzar_fila(numero_fila_actual)
            fila = historial[numero_fila_actual]

        if datos_usuario.get('iag'):
            alicuota_global = float(datos_usuario['alicuota'] or 0)
            importe_iag = imp_neto_total * alicuota_global / 100

            tributos.append([
                datos_usuario['id_tributo_global'],
                datos_usuario['desc_iag'],
                imp_neto_total,
                alicuota_global,
                importe_iag,
                None
            ])

        return tributos
        
    def transformar_a_tipos_correctos(self, datos_factura):
        datos_factura[constantes_array_biblioteca_factura.identificador_factura.value] = int(datos_factura[constantes_array_biblioteca_factura.identificador_factura.value] or 0)
        datos_factura[constantes_array_biblioteca_factura.tipo_factura_nota.value] = str(datos_factura[constantes_array_biblioteca_factura.tipo_factura_nota.value] or "")
        datos_factura[constantes_array_biblioteca_factura.tipo_documento.value] = str(datos_factura[constantes_array_biblioteca_factura.tipo_documento.value] or "")
        datos_factura[constantes_array_biblioteca_factura.numero_de_documento_del_cliente.value] = int(datos_factura[constantes_array_biblioteca_factura.numero_de_documento_del_cliente.value] or 0)
        datos_factura[constantes_array_biblioteca_factura.nombre_y_apellido_cliente.value] = str(datos_factura[constantes_array_biblioteca_factura.nombre_y_apellido_cliente.value] or "")
        datos_factura[constantes_array_biblioteca_factura.telefono.value] = str(datos_factura[constantes_array_biblioteca_factura.telefono.value] or "")
        datos_factura[constantes_array_biblioteca_factura.provincia.value] = str(datos_factura[constantes_array_biblioteca_factura.provincia.value] or "")
        datos_factura[constantes_array_biblioteca_factura.localidad.value] = str(datos_factura[constantes_array_biblioteca_factura.localidad.value] or "")
        datos_factura[constantes_array_biblioteca_factura.domicilio.value] = str(datos_factura[constantes_array_biblioteca_factura.domicilio.value] or "")
        datos_factura[constantes_array_biblioteca_factura.condicion_de_venta_cliente.value] = str(datos_factura[constantes_array_biblioteca_factura.condicion_de_venta_cliente.value] or "")
        datos_factura[constantes_array_biblioteca_factura.condicion_frente_al_iva_cliente.value] = str(datos_factura[constantes_array_biblioteca_factura.condicion_frente_al_iva_cliente.value] or "")
        datos_factura[constantes_array_biblioteca_factura.concepto.value] = str(datos_factura[constantes_array_biblioteca_factura.concepto.value] or "")
        datos_factura[constantes_array_biblioteca_factura.fecha_servicio_desde.value] = str(datos_factura[constantes_array_biblioteca_factura.fecha_servicio_desde.value] or "")
        datos_factura[constantes_array_biblioteca_factura.fecha_servicio_hasta.value] = str(datos_factura[constantes_array_biblioteca_factura.fecha_servicio_hasta.value] or "")
        datos_factura[constantes_array_biblioteca_factura.fecha_vencimiento_de_pago.value] = str(datos_factura[constantes_array_biblioteca_factura.fecha_vencimiento_de_pago.value] or "")
        datos_factura[constantes_array_biblioteca_factura.importe_neto.value] = float(datos_factura[constantes_array_biblioteca_factura.importe_neto.value] or 0.0)
        datos_factura[constantes_array_biblioteca_factura.importe_total.value] = float(datos_factura[constantes_array_biblioteca_factura.importe_total.value] or 0.0)
        datos_factura[constantes_array_biblioteca_factura.importe_tributo.value] = float(datos_factura[constantes_array_biblioteca_factura.importe_tributo.value] or 0.0)
        datos_factura[constantes_array_biblioteca_factura.base_imponible_sin_21.value] = int(datos_factura[constantes_array_biblioteca_factura.base_imponible_sin_21.value])
        datos_factura[constantes_array_biblioteca_factura.base_imponible_sin_105.value] = int(datos_factura[constantes_array_biblioteca_factura.base_imponible_sin_105.value])
        datos_factura[constantes_array_biblioteca_factura.base_imponible_0.value] = int(datos_factura[constantes_array_biblioteca_factura.base_imponible_0.value])
        datos_factura[constantes_array_biblioteca_factura.importe_iva_21.value] = int(datos_factura[constantes_array_biblioteca_factura.importe_iva_21.value] or 0)
        datos_factura[constantes_array_biblioteca_factura.importe_iva_105.value] = int(datos_factura[constantes_array_biblioteca_factura.importe_iva_105.value] or 0)

    def obtener_datos_factura(self, datos_form, datos_formateados):
        for i in range(constantes_historial.pos_Identificador_Factura.value-1, constantes_historial.pos_Fecha_Vencimiento_Pago.value-1):
            datos_formateados.append(datos_form[i])