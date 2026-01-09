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
    col_ultimo_dato_facturacion = pos_Cantidad

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
