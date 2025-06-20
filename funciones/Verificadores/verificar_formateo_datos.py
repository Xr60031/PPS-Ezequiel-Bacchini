def verificar_formateo_datos(datos_factura):
    return(
        isinstance(datos_factura["Identificador_Factura"],int) and
        isinstance(datos_factura["tipo_factura_nota"],str) and
        isinstance(datos_factura["Nombre_y_Apellido_Cliente"],str) and
        isinstance(datos_factura["Tipo_Documento"],str) and
        isinstance(datos_factura["Numero_de_documento_del_cliente"],int) and
        isinstance(datos_factura["Condicion_de_venta_Cliente"],str) and
        isinstance(datos_factura["Condicion_frente_al_IVA_Cliente"],str) and
        isinstance(datos_factura["Concepto"],str) and
        isinstance(datos_factura["Fecha_servicio_desde"],(str, type(None))) and
        isinstance(datos_factura["Fecha_servicio_hasta"],(str, type(None))) and
        isinstance(datos_factura["Fecha_vencimiento_de_pago"],(str, type(None))) and
        isinstance(datos_factura["ID_doc"],int) and
        isinstance(datos_factura["ID_concepto"],int) and
        isinstance(datos_factura["ID_factura_nota"],int) and
        isinstance(datos_factura["ID_IVA_cliente"],int) and
        isinstance(datos_factura["Importe_Neto"], (float, type(None))) and
        isinstance(datos_factura["Importe_Total"], (float, type(None))) and
        isinstance(datos_factura["Importe_Tributo"], (float, type(None))) and
        isinstance(datos_factura["tributos"], (list, type(None))) and
        isinstance(datos_factura["items"], list,) and
        isinstance(datos_factura["nro_cbte_anular"], (int, type(None))) and
        isinstance(datos_factura["fecha_emision"], str)
    )

if __name__ == '__main__':
    datos_factura = {
        'Identificador_Factura': 1,
        'tipo_factura_nota': 'Factura C',
        'Nombre_y_Apellido_Cliente': 'Ezequiel Bacchini',
        'Tipo_Documento': 'DNI',
        'Numero_de_documento_del_cliente': 46266831,
        'Condicion_de_venta_Cliente': 'Contado',
        'Condicion_frente_al_IVA_Cliente': 'Consumidor Final',
        'Concepto': 'PRODUCTOS',
        'Fecha_servicio_desde': '2025-06-17',
        'Fecha_servicio_hasta': '2025-06-17',
        'Fecha_vencimiento_de_pago': '2025-06-17',
        'ID_doc': 96,
        'ID_concepto': 1,
        'ID_factura_nota': 11,
        'ID_IVA_cliente': 5,
        'Importe_Neto': 61.9685,
        'Importe_Total': 66.3785,
        'Importe_Tributo': 4.410000000000004,
        'tributos': [
            [6, 'Impuesto BK', 0, 21.0, 4.41, 'Agua Mineral Tres']
        ],
        'items': [
            ['Agua Mineral Uno', 0, 1, 'AGUA01', 'Es Agua Mineral', 20.0, None, 20.0, 20.0],
            ['Agua Mineral Dos', 0.15, 1, 'AGUA02', 'Es también agua mineral', 21.0, None, 20.9685, 20.9685],
            ['Agua Mineral Tres', 0, 1, 'AGUA03', 'Es Agua Mineral de lujo', 21.0, 'Percepción de IVA', 21.0, 25.41]
        ],
        'nro_cbte_anular': None,
        'fecha_emision': '20250617'
    }

    print(verificar_formateo_datos(datos_factura))