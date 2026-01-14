from enum import Enum, auto

class workbooks(Enum):
    facturaA = "Factura_A"
    facturaB = "Factura_B"
    facturaC = "Factura_C"
    contactos_frecuentes = "Contactos_Frecuentes"
    historial = "Historial"
    items = "Items"
    xml = "XML"
    datos = "Datos"

    cantidad_hojas = 8

class constantes_genericas_excel(Enum):
    starting_row = 2
    starting_colvar = 1

class constantes_clientes_frecuentes_excel(Enum):
    nombre_apellido = 1
    tipo_documento = auto() 
    numero_documento = auto()   
    numero_telefono = auto()   
    provincia = auto()   
    localidad = auto()   
    domicilio = auto()
    condicion_iva = auto()   
    cantidad_total_variables_cliente = auto()


class constantes_xml_excel(Enum):
    starting_row = 1
    starting_colvar = 1

class constantes_posicion_datos_factura_excel(Enum):
    pos_Identificador_Factura = 1                # Identificador Factura 
    pos_Tipo_de_Factura = auto()                 # Tipo de Factura 
    pos_Tipo_Documento = auto()                  # Tipo Documento 
    pos_Numero_de_documento_del_cliente = auto() # Número de documento del cliente 
    pos_Nombre_y_Apellido_Cliente = auto()       # Nombre y Apellido Cliente 
    pos_Telefono = auto()                         # Telefono 
    pos_Provincia = auto()                        # Provincia 
    pos_Localidad = auto()                        # Localidad 
    pos_Direccion = auto()                        # Dirección 
    pos_Condicion_venta_cliente = auto()         # Condicion venta cliente 
    pos_Condicion_IVA_cliente = auto()           # Condicion IVA cliente 
    pos_Concepto = auto()                        # Concepto 
    pos_Fecha_servicio_desde = auto()            # Fecha Servicio desde 
    pos_Fecha_servicio_hasta = auto()            # Fecha servicio hasta 
    pos_Fecha_vencimiento_de_pago = auto()       # Fecha vencimiento de pago 
    pos_Producto_Servicio = auto()               # Producto/Servicio 
    pos_Porcentaje_bonificado = auto()           # Porcentaje bonificado (%) 
    pos_Cantidad = auto()                         # Cantidad

    #Ultima columna previo a que las columnas esten vacias en la hoja de facturacion
    col_ultimo_dato_facturacion = auto()

class constantes_posicion_items_excel(Enum):
    pos_Producto_Servicio = 1      # Producto/Servicio
    pos_Codigo = auto()             # Código
    pos_Descripcion = auto()        # Descripción
    pos_Precio_Unitario = auto()    # Precio Unitario
    pos_Impuesto_Adicional = auto() # Impuesto Adicional
    pos_Descripcion_Impuesto = auto() # Descripción del impuesto
    pos_Alicuota = auto()           # Alícuota (%)

class constantes_posicion_datos_usuario_excel(Enum):
    pos_Nombre = 1                         # nombre 1
    pos_CUIT = auto()                       # cuit 2 
    pos_Nombre_Empresa = auto()             # nombre empresa 3
    pos_Punto_Venta = auto()                # punto venta 4
    pos_Razon_Social = auto()               # razon social 5
    pos_Domicilio = auto()                  # domicilio 6
    pos_Condicion_IVA_Vendedor = auto()     # condicion iva vendedor 7
    pos_Ingresos_Brutos = auto()            # ingresos brutos 8
    pos_Fecha_Inicio = auto()               # fecha inicio 9
    pos_Impuesto_Adicional_Global = auto()  # impuesto adicional global 10
    pos_Descripcion_IAG = auto()            # descripcion iag 11 
    pos_Alicuota = auto()                   # alicuota 12

from enum import Enum, auto

class constantes_historial(Enum):
    pos_Identificador_Factura = 1
    pos_Tipo_Factura_Nota = auto()
    pos_Tipo_Documento = auto()
    pos_Numero_Documento_Cliente = auto()
    pos_Nombre_Apellido_Cliente = auto()
    pos_Telefono = auto()
    pos_Provincia = auto()
    pos_Localidad = auto()
    pos_Domicilio = auto()
    pos_Condicion_Venta_Cliente = auto()
    pos_Condicion_IVA_Cliente = auto()
    pos_Concepto = auto()
    pos_Fecha_Servicio_Desde = auto()
    pos_Fecha_Servicio_Hasta = auto()
    pos_Fecha_Vencimiento_Pago = auto()
    pos_Producto_Servicio = auto()
    pos_Porcentaje_Bonificado = auto()
    pos_Cantidad = auto()
    pos_Codigo_Producto = auto()
    pos_Descripcion = auto()
    pos_Precio_Unitario = auto()
    pos_Impuesto_Adicional = auto()
    pos_Importe_Bonificado = auto()
    pos_Subtotal = auto()
    pos_Importe_Neto = auto()
    pos_Importe_Total = auto()
    pos_Importe_Tributo = auto()
    pos_Descripcion_Impuesto_Adicional = auto()
    pos_Alicuota_Impuesto_Adicional = auto()
    pos_Nombre_Apellido_Vendedor = auto()
    pos_CUIT_Vendedor = auto()
    pos_Nombre_Empresa = auto()
    pos_Punto_Venta = auto()
    pos_Razon_Social = auto()
    pos_Domicilio_Vendedor = auto()
    pos_Condicion_Frente_IVA = auto()
    pos_Ingresos_Brutos = auto()
    pos_Fecha_Inicio = auto()
    pos_Impuesto_Adicional_Global = auto()
    pos_Descripcion_Impuesto_Adicional_Global = auto()
    pos_Alicuota_Global = auto()
    pos_CAE_Numero = auto()
    pos_CAE_Fecha_Vencimiento = auto()
    pos_Numero_Comprobante = auto()
    pos_base_21 = auto()
    pos_base_105 = auto()
    pos_base_0 = auto()
    pos_Alicuota_21 = auto()
    pos_Alicuota_10_5 = auto()
    pos_Ultimo_Dato = auto()
