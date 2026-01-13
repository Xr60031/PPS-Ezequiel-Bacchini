from enum import Enum, auto

class constantes_configuracion(Enum):
    pos_nombre_apellido = 0
    pos_cuit = auto()
    pos_nombre_empresa = auto()
    pos_pventa = auto()             #Punto de venta
    pos_razon_social = auto()
    pos_domicilio = auto()
    pos_condicion_IVA = auto()
    pos_ingresos_brutos = auto()
    pos_fecha_inicio = auto()
    pos_iag = auto()                #Impuesto Adicional Global
    pos_diag = auto()               #Descripcion impuesto adicional global
    pos_alicuota = auto()

class constantes_historial(Enum):
    excel_dataframe = 0
    excel_hoja_historial = auto()

class constantes_CAE(Enum):
    CAE = 0
    CAE_vencimiento = auto()
    ultimo_comprobante_autorizado = auto()

class constantes_PDF(Enum):
    ultimo_comprobante_autorizado = 0
    pos_contenido_pdf = auto()

class constantes_armador_historial(Enum):
    IDENTIFICADOR_FACTURA = 0
    TIPO_FACTURA_NOTA = auto()
    TIPO_DOCUMENTO = auto()
    NUMERO_DE_DOCUMENTO_DEL_CLIENTE = auto()
    NOMBRE_Y_APELLIDO_CLIENTE = auto()
    TELEFONO_CLIENTE = auto()
    PROVINCIA_CLIENTE = auto()
    LOCALIDAD_CLIENTE = auto()
    DIRECCION_CLIENTE = auto()
    CONDICION_DE_VENTA_CLIENTE = auto()
    CONDICION_FRENTE_AL_IVA_CLIENTE = auto()
    CONCEPTO = auto()
    FECHA_SERVICIO_DESDE = auto()
    FECHA_SERVICIO_HASTA = auto()
    FECHA_VENCIMIENTO_DE_PAGO = auto()
    PRODUCTOS_SERVICIOS = auto()
    IMPORTE_NETO = auto()
    IMPORTE_TOTAL = auto()
    IMPORTE_TRIBUTO = auto()
    TRIBUTOS = auto()
    VENDEDOR_NOMBRE = auto()
    VENDEDOR_CUIT = auto()
    VENDEDOR_NOMBRE_EMPRESA = auto()
    VENDEDOR_PUNTO_DE_VENTA = auto()
    VENDEDOR_RAZON_SOCIAL = auto()
    VENDEDOR_DOMICILIO = auto()
    VENDEDOR_CONDICION_FRENTE_AL_IVA = auto()
    VENDEDOR_INGRESOS_BRUTOS = auto()
    VENDEDOR_FECHA_INICIO = auto()
    VENDEDOR_IAG = auto()
    VENDEDOR_DESC_IAG = auto()
    VENDEDOR_ALICUOTA = auto()
    CAE = auto()
    CAE_VENCIMIENTO = auto()
    ULTIMO_COMPROBANTE_AUTORIZADO = auto()
    ALICUOTA_21 = auto()
    ALICUOTA_10_5 = auto()

    #Cantidad de variables hasta llegar a productos/servicios
    limite_hasta_items = PRODUCTOS_SERVICIOS
    #Cantidad de datos que tiene un producto o servicio
    cant_datos_items = 9
    #Cantidad de variables hasta llegar a tributos
    limite_hasta_tributos = limite_hasta_items + cant_datos_items
    #Cantidad de datos que tiene un tributo y son efectivamente utilizados al escribir un historial
    cant_datos_tributos_utilizados = 2
    #Distancia entre items e tributos
    distancia_entre_tributos_items = 4

    #Columna de ID de factura en el Excel
    columna_id_excel = 1
    #Columna de Producto/Servicio de factura en el Excel
    columna_item = PRODUCTOS_SERVICIOS

class constantes_array_datos_factura(Enum):
    pos_ID = 0
    pos_tipo_factura_nota = auto()
    pos_Tipo_Documento = auto()
    pos_Numero_de_documento_del_cliente = auto()
    pos_Nombre_y_Apellido_Cliente = auto()
    pos_Telefono = auto()                     
    pos_Provincia = auto()                        
    pos_Localidad = auto()                       
    pos_Direccion = auto()                        
    pos_Condicion_de_venta_Cliente = auto()
    pos_Condicion_frente_al_IVA_Cliente = auto()
    pos_Concepto = auto()
    pos_Fecha_servicio_desde = auto()
    pos_Fecha_servicio_hasta = auto()
    pos_Fecha_vencimiento_de_pago = auto()
    pos_Importe_Neto = auto()
    pos_Importe_Total = auto()
    pos_Importe_Tributo = auto()
    pos_tributos = auto()
    pos_items = auto()

    #Ultima columna antes de datos de productos
    pos_ultimo_dato_antes_de_productos = pos_Fecha_vencimiento_de_pago

class constantes_vendedor(Enum):
    NOMBRE = 0
    CUIT = auto()
    NOMBRE_EMPRESA = auto()
    PUNTO_VENTA = auto()
    RAZON_SOCIAL = auto()
    DOMICILIO = auto()
    CONDICION_IVA_VENDEDOR = auto()
    INGRESOS_BRUTOS = auto()
    FECHA_INICIO = auto()
    IMPUESTO_ADICIONAL_GLOBAL = auto()
    DESCRIPCION_IAG = auto()
    ALICUOTA = auto()


class constantes_obtenedor_datos_item(Enum):
    pos_codigo_producto = 0
    pos_descripcion = auto()
    pos_precio_unitario = auto()
    pos_impuesto_adicional = auto()
    pos_descripcion_tributo_adicional = auto()
    pos_alicuota = auto()
    pos_importe_bonificado = auto()
    pos_subtotal = auto()

class constantes_obtenedor_datos(Enum):
    pos_cantidad = 0
    pos_porcentaje_bonificado = auto()
    pos_nombre_producto_servicio = auto()


class constantes_factura(Enum):
    identificador_factura = 0
    tipo_factura_nota = auto()
    tipo_documento = auto()
    numero_de_documento_del_cliente = auto()
    nombre_y_apellido_cliente = auto()
    telefono = auto()
    provincia = auto()
    localidad = auto()
    domicilio = auto()
    condicion_de_venta_cliente = auto()
    condicion_frente_al_iva_cliente = auto()
    concepto = auto()
    fecha_servicio_desde = auto()
    fecha_servicio_hasta = auto()
    fecha_vencimiento_de_pago = auto()
    importe_neto = auto()
    importe_total = auto()
    importe_tributo = auto()
    tributos = auto()
    items = auto()
    base_imponible_sin_21 = auto()
    importe_iva_21 = auto()
    base_imponible_sin_105 = auto()
    importe_iva_105 = auto()
    base_imponible_0 = auto()

class constantes_array_datos_factura_FM(Enum):
    #pos_tributos array position in datos_factura
    pos_tributos = 11
    #pos_items array position in datos_factura
    pos_items = auto()