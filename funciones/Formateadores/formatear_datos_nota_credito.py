import json as json_biblioteca
from Constantes import constantes_nota_credito

def transformar_a_lista(data_source):
        if data_source:
            return json_biblioteca.loads(data_source)
    
def transformar_a_tipos_correctos(datos_factura):
    datos_factura[constantes_nota_credito.pos_ID] = int(datos_factura[constantes_nota_credito.pos_ID])
    datos_factura[constantes_nota_credito.pos_tipo_factura_nota] = str(datos_factura[constantes_nota_credito.pos_tipo_factura_nota])
    datos_factura[constantes_nota_credito.pos_Nombre_y_Apellido_Cliente] = str(datos_factura[constantes_nota_credito.pos_Nombre_y_Apellido_Cliente])
    datos_factura[constantes_nota_credito.pos_tipo_documento] = str(datos_factura[constantes_nota_credito.pos_tipo_documento])
    datos_factura[constantes_nota_credito.pos_numero_documento_cliente] = int(datos_factura[constantes_nota_credito.pos_numero_documento_cliente])
    datos_factura[constantes_nota_credito.pos_condicion_venta_cliente] = str(datos_factura[constantes_nota_credito.pos_condicion_venta_cliente])
    datos_factura[constantes_nota_credito.pos_condicion_iva_cliente] = str(datos_factura[constantes_nota_credito.pos_condicion_iva_cliente])
    datos_factura[constantes_nota_credito.pos_concepto] = str(datos_factura[constantes_nota_credito.pos_concepto])
    datos_factura[constantes_nota_credito.pos_fecha_servicio_desde] = str(datos_factura[constantes_nota_credito.pos_fecha_servicio_desde])
    datos_factura[constantes_nota_credito.pos_fecha_servicio_hasta] = str(datos_factura[constantes_nota_credito.pos_fecha_servicio_hasta])
    datos_factura[constantes_nota_credito.pos_fecha_vencimiento_pago] = str(datos_factura[constantes_nota_credito.pos_fecha_vencimiento_pago])
    datos_factura[constantes_nota_credito.pos_producto_servicio] = str(datos_factura[constantes_nota_credito.pos_producto_servicio])
    datos_factura[constantes_nota_credito.pos_porcentaje_bonificado] = float(datos_factura[constantes_nota_credito.pos_porcentaje_bonificado]) or 0.0
    datos_factura[constantes_nota_credito.pos_cantidad] = int(datos_factura[constantes_nota_credito.pos_cantidad])
    datos_factura[constantes_nota_credito.pos_codigo_producto] = str(datos_factura[constantes_nota_credito.pos_codigo_producto]) or None
    datos_factura[constantes_nota_credito.pos_descripcion] = str(datos_factura[constantes_nota_credito.pos_descripcion]) or None
    datos_factura[constantes_nota_credito.pos_precio_unitario] = float(datos_factura[constantes_nota_credito.pos_precio_unitario])
    datos_factura[constantes_nota_credito.pos_impuesto_adicional] = str(datos_factura[constantes_nota_credito.pos_impuesto_adicional]) or None
    datos_factura[constantes_nota_credito.pos_importe_bonificado] = float(datos_factura[constantes_nota_credito.pos_importe_bonificado]) or None
    datos_factura[constantes_nota_credito.pos_subtotal] = float(datos_factura[constantes_nota_credito.pos_subtotal])
    datos_factura[constantes_nota_credito.pos_importe_neto] = float(datos_factura[constantes_nota_credito.pos_importe_neto])
    datos_factura[constantes_nota_credito.pos_importe_total] = float(datos_factura[constantes_nota_credito.pos_importe_total])
    datos_factura[constantes_nota_credito.pos_importe_tributo] = float(datos_factura[constantes_nota_credito.pos_importe_tributo]) or None
    datos_factura[constantes_nota_credito.pos_descripcion_impuesto_adicional] = str(datos_factura[constantes_nota_credito.pos_descripcion_impuesto_adicional]) or None
    datos_factura[constantes_nota_credito.pos_alicuota_impuesto_adicional] = int(datos_factura[constantes_nota_credito.pos_alicuota_impuesto_adicional]) or None
    datos_factura[constantes_nota_credito.pos_nombre_apellido_vendedor] = str(datos_factura[constantes_nota_credito.pos_nombre_apellido_vendedor])
    datos_factura[constantes_nota_credito.pos_cuit_vendedor] = int(datos_factura[constantes_nota_credito.pos_cuit_vendedor])
    datos_factura[constantes_nota_credito.pos_nombre_empresa] = str(datos_factura[constantes_nota_credito.pos_nombre_empresa])
    datos_factura[constantes_nota_credito.pos_punto_venta] = int(datos_factura[constantes_nota_credito.pos_punto_venta])
    datos_factura[constantes_nota_credito.pos_razon_social] = str(datos_factura[constantes_nota_credito.pos_razon_social])
    datos_factura[constantes_nota_credito.pos_domicilio] = str(datos_factura[constantes_nota_credito.pos_domicilio])
    datos_factura[constantes_nota_credito.pos_condicion_frente_iva] = str(datos_factura[constantes_nota_credito.pos_condicion_frente_iva])
    datos_factura[constantes_nota_credito.pos_ingresos_brutos] = int(datos_factura[constantes_nota_credito.pos_ingresos_brutos])
    datos_factura[constantes_nota_credito.pos_fecha_inicio] = str(datos_factura[constantes_nota_credito.pos_fecha_inicio])
    datos_factura[constantes_nota_credito.pos_impuesto_adicional_global] = str(datos_factura[constantes_nota_credito.pos_impuesto_adicional_global])
    datos_factura[constantes_nota_credito.pos_descripcion_impuesto_adicional_global] = str(datos_factura[constantes_nota_credito.pos_descripcion_impuesto_adicional_global])
    datos_factura[constantes_nota_credito.pos_alicuota_global] = int(datos_factura[constantes_nota_credito.pos_alicuota_global])
    datos_factura[constantes_nota_credito.pos_cae_numero] = int(datos_factura[constantes_nota_credito.pos_cae_numero])
    datos_factura[constantes_nota_credito.pos_cae_fecha_vencimiento] = str(datos_factura[constantes_nota_credito.pos_cae_fecha_vencimiento])
    datos_factura[constantes_nota_credito.pos_numero_comprobante] = int(datos_factura[constantes_nota_credito.pos_numero_comprobante])

def obtener_datos_factura(datos_form, datos_formateados):
    for i in range(constantes_nota_credito.pos_ID, constantes_nota_credito.pos_fecha_vencimiento_pago):
        datos_formateados.append(datos_form[i])