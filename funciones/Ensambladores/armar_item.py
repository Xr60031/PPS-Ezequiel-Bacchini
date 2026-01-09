from Funciones.ID.obtenerdor_IDs import Obtenedor_ID
from Constantes.Facturacion.constantes_arrays import constantes_obtenedor_datos_item, constantes_obtenedor_datos

class Armador_Item():
    def __init__(self):
        self

    def armar_datos_producto_servicio(self, productos_servicios, tributos, datos_hoja_factura, datos_hoja_item):
        productos_y_servicios_actual = [
            datos_hoja_factura[constantes_obtenedor_datos.pos_nombre_producto_servicio.value],  # 0 - Producto/Servicio
            datos_hoja_factura[constantes_obtenedor_datos.pos_porcentaje_bonificado.value],  # 1 - Porcentaje Bonificado
            datos_hoja_factura[constantes_obtenedor_datos.pos_cantidad.value],  # 2 - Cantidad
            datos_hoja_item[constantes_obtenedor_datos_item.pos_codigo_producto.value],  # 3 - Código Producto
            datos_hoja_item[constantes_obtenedor_datos_item.pos_descripcion.value],  # 4 - Descripción
            datos_hoja_item[constantes_obtenedor_datos_item.pos_precio_unitario.value],  # 5 - Precio Unitario
            datos_hoja_item[constantes_obtenedor_datos_item.pos_impuesto_adicional.value],  # 6 - Impuesto Adicional
            datos_hoja_item[constantes_obtenedor_datos_item.pos_importe_bonificado.value],  # 7- Importe Bonificado
            datos_hoja_item[constantes_obtenedor_datos_item.pos_subtotal.value], # 8- Subtotal
        ] 

        productos_servicios.append(productos_y_servicios_actual)

        obtenedor_id = Obtenedor_ID()
        id_tributo = obtenedor_id.obtener_ID_tributo(datos_hoja_item[constantes_obtenedor_datos_item.pos_impuesto_adicional.value])
        if(id_tributo):

            tributos_actual = [
                id_tributo, # 0 - ID_tributo
                datos_hoja_item[constantes_obtenedor_datos_item.pos_descripcion_tributo_adicional.value], # 1 - descripcion_impuesto_adicional
                datos_hoja_item[constantes_obtenedor_datos_item.pos_importe_bonificado.value], # 2 -Importe Bonificado
                datos_hoja_item[constantes_obtenedor_datos_item.pos_alicuota.value], # 3 - alicuota_impuesto_adicional
                0, # 4 - Importe tributo
                datos_hoja_factura[constantes_obtenedor_datos.pos_nombre_producto_servicio.value] # 5 -ID_relacionada_a_producto
            ]
            tributos.append(tributos_actual)

        return