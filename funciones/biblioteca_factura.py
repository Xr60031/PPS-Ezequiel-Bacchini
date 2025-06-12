from Funciones.obtenerdor_IDs import obtener_ID_concepto, obtener_ID_condicion_iva_cliente, obtener_ID_documento, obtener_ID_Factura
from datetime import datetime

#Arma la biblioteca con los datos de la factura
def armar_biblioteca_factura(datos_factura):
    datos_factura = {
        "Identificador_Factura": datos_factura[0],
        "tipo_factura_nota": datos_factura[1],
        "Nombre_y_Apellido_Cliente": datos_factura[2],
        "Tipo_Documento": datos_factura[3],
        "Numero_de_documento_del_cliente": int(datos_factura[4]),
        "Condicion_de_venta_Cliente": datos_factura[5],
        "Condicion_frente_al_IVA_Cliente": datos_factura[6],
        "Concepto": datos_factura[7],
        "Fecha_servicio_desde": datos_factura[8],
        "Fecha_servicio_hasta": datos_factura[9],
        "Fecha_vencimiento_de_pago": datos_factura[10],
        "ID_doc": obtener_ID_documento(datos_factura[3]),
        "ID_concepto": obtener_ID_concepto(datos_factura[7]),
        "ID_factura_nota": obtener_ID_Factura(datos_factura[1]),
        "ID_IVA_cliente": obtener_ID_condicion_iva_cliente(datos_factura[6]),
        "Importe_Neto": 0,
        "Importe_Total": 0,
        "Importe_Tributo": 0,
        "tributos": 0,
        "items": 0,
        "nro_cbte_anular" : None,
        "fecha_emision" : datetime.now()
    }
    return datos_factura

def set_comprobante_anular(datos_factura, cbte_anular):
    datos_factura["nro_cbte_anular"] = cbte_anular