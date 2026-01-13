from enum import Enum, auto

class constantes_posicion_items(Enum):
    #Producto/Servicio array position in productos_servicios
    pos_producto_servicio = 0
    #Porcentaje Bonificado array position in productos_servicios
    pos_porcentaje_bonificado = auto()
    #Cantidad array position in productos_servicios
    pos_cantidad = auto()
    #Código Producto array position in productos_servicios
    pos_codigo_producto = auto()
    #Descripción array position in productos_servicios
    pos_descripcion_producto = auto()
    #Precio Unitario array position in productos_servicios
    pos_precio_unitario = auto()
    #Impuesto Adicional array position in productos_servicios
    pos_impuesto_adicional = auto()
    #Importe Bonificado array position in productos_servicios
    pos_importe_bonificado = auto()
    #Subtotal array position in productos_servicios
    pos_subtotal = auto()

    #Contiene la cantidad de datos que posee cada item (En donde se usa es -2 al ser cant total items +1 y empezando los arrays en 0)
    cantidad_total_datos_por_item = auto()

    pos_alicuota_auxiliar = auto()

class constantes_posicion_tributos(Enum):
    #ID_tributo array position in tributos
    pos_ID_tributo=0
    #descripcion_impuesto_adicional array position in tributos
    pos_descripcion_impuesto_adicional = auto()
    #precio_bonificado array position in tributos
    pos_precio_bonificado = auto()
    #alicuota_impuesto_adicional array position in tributos
    pos_alicuota_impuesto_adicional = auto()
    #importe_tributo array position in tributos
    pos_importe_tributo = auto()
    #pos_id_relacionado_tributo array position in tributos
    pos_id_relacionado_tributo = auto()