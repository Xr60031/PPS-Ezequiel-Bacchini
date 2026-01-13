from Constantes.Facturacion.constantes_arrays import constantes_CAE
class Armador_Historial():
    def __init__(self):
        self

    #Builea el array que contiene todos los datos para que sean escritos en el historial
    def build_datos_historial(self, datos_historial, datos_factura, productos_servicios, tributos, biblioteca_datos_vendedor, datos_cae):
        datos_historial.append(datos_factura["Identificador_Factura"])
        datos_historial.append(datos_factura["tipo_factura_nota"])
        datos_historial.append(datos_factura["Tipo_Documento"])
        datos_historial.append(datos_factura["Numero_de_documento_del_cliente"])
        datos_historial.append(datos_factura["Nombre_y_Apellido_Cliente"])
        datos_historial.append(datos_factura["Telefono"])
        datos_historial.append(datos_factura["Localidad"])
        datos_historial.append(datos_factura["Provincia"])
        datos_historial.append(datos_factura["Direccion"])
        datos_historial.append(datos_factura["Condicion_de_venta_Cliente"])
        datos_historial.append(datos_factura["Condicion_frente_al_IVA_Cliente"])
        datos_historial.append(datos_factura["Concepto"])
        datos_historial.append(datos_factura["Fecha_servicio_desde"])
        datos_historial.append(datos_factura["Fecha_servicio_hasta"])
        datos_historial.append(datos_factura["Fecha_vencimiento_de_pago"])
        datos_historial.append(productos_servicios)
        datos_historial.append(datos_factura["Importe_Neto"])
        datos_historial.append(datos_factura["Importe_Total"])
        datos_historial.append(datos_factura["Importe_Tributo"])
        datos_historial.append(tributos)
        datos_historial.append(biblioteca_datos_vendedor["Nombre"])
        datos_historial.append(biblioteca_datos_vendedor["CUIT"])
        datos_historial.append(biblioteca_datos_vendedor["Nombre_Empresa"])
        datos_historial.append(biblioteca_datos_vendedor["Punto_de_venta"])
        datos_historial.append(biblioteca_datos_vendedor["Razon_Social"])
        datos_historial.append(biblioteca_datos_vendedor["Domicilio"])
        datos_historial.append(biblioteca_datos_vendedor["Condicion_frente_al_IVA"])
        datos_historial.append(biblioteca_datos_vendedor["Ingresos_Brutos"])
        datos_historial.append(biblioteca_datos_vendedor["Fecha_Inicio"])
        datos_historial.append(biblioteca_datos_vendedor["iag"])
        datos_historial.append(biblioteca_datos_vendedor["desc_iag"])
        datos_historial.append(biblioteca_datos_vendedor["alicuota"])
        datos_historial.append(datos_cae[constantes_CAE.CAE.value]),
        datos_historial.append(datos_cae[constantes_CAE.CAE_vencimiento.value]),
        datos_historial.append(datos_cae[constantes_CAE.ultimo_comprobante_autorizado.value])
        datos_historial.append(datos_factura["Base_Imponible_sin_21%"])
        datos_historial.append(datos_factura["Base_Imponible_sin_10.5%"])
        datos_historial.append(datos_factura["Base_Imponible_0%"])
        datos_historial.append(datos_factura["Importe_IVA_21%"])
        datos_historial.append(datos_factura["Importe_IVA_10.5%"])
        return