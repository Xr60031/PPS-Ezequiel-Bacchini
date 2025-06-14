from Funciones.Obtener_datos_facturacion.obtenedor_datos_facturacion import obtenedor_datos_facturacion
import json as json_biblioteca
from Funciones.formatear_items_FU import formatear_items_facturador_unico, agregar_items_tributos_resultados

class Obtenedor_FU(obtenedor_datos_facturacion):
    def __init__(self):
        super().__init__()

    def obtener_datos_facturacion(self, data_source, datos_factura_manager, datos_usuario):
        items = data_source.form.getlist("selected_item")
        items_dict = [json_biblioteca.loads(p) for p in items]
        items_formateados = []
        tributos_formateados = []
        formatear_items_facturador_unico(items_dict, items_formateados, tributos_formateados)
        datos_form = []
        datos_form.append(data_source.form.get("id_factura"))
        datos_form.append(data_source.form.get("tipo_factura"))
        datos_form.append(data_source.form.get("nombre_apellido_cliente"))
        datos_form.append(data_source.form.get("tipo_doc"))
        datos_form.append(data_source.form.get("numero_doc_cliente"))
        datos_form.append(data_source.form.get("concepto_venta"))
        datos_form.append(data_source.form.get("concepto_iva"))
        datos_form.append(data_source.form.get("concepto"))
        datos_form.append(data_source.form.get("fecha_desde"))
        datos_form.append(data_source.form.get("fecha_hasta"))
        datos_form.append(data_source.form.get("fecha_vto_pago"))
        datos_form = datos_factura_manager.armar_biblioteca_factura(datos_form)
        agregar_items_tributos_resultados(items_formateados, tributos_formateados, datos_form, datos_usuario)
        datos_factura = []
        datos_factura.append(datos_form)
        return datos_factura