from openpyxl import load_workbook
from ExcelManager.obtener_datos_hoja_factura_actual import obtener_datos_hoja_factura_item_actual
from ExcelManager.obtener_datos_hoja_item_actual import obtener_datos_hoja_item_actual
from Funciones.armar_item import armar_datos_producto_servicio
from Constantes import constantes_dato_factura

def obtener_ID(factura_hoja, row):
    return factura_hoja.cell(row=row, column=1).value

def obtener_productos_servicios(excel_dataframe, datos_factura, row, productos_servicios, tributos): 
    ID = datos_factura[constantes_dato_factura.pos_ID]
    ID_anterior = ID
    hoja_actual = excel_dataframe["Facturas_A_Realizar"]

    while ID == ID_anterior and ID != "" :
        datos_hoja_factura = obtener_datos_hoja_factura_item_actual(hoja_actual, row)
        hoja_actual = excel_dataframe["Items"]
        datos_hoja_item = obtener_datos_hoja_item_actual(hoja_actual, datos_hoja_factura)
        armar_datos_producto_servicio(productos_servicios, tributos, datos_hoja_factura, datos_hoja_item)
        
        ID_anterior = ID
        row += 1
        hoja_actual = excel_dataframe["Facturas_A_Realizar"]
        ID = obtener_ID(hoja_actual, row) 

#Abre la plantilla de excel y devuelve una lista con todos los datos que el sistema necesita para facturar
def obtener_datos_factura(filename):
    excel_dataframe=load_workbook(filename, data_only=True)
    factura_hoja=excel_dataframe["Facturas_A_Realizar"]
    row = 2
    cant_var = 1
    datos_facturas_total = []

    ID = factura_hoja.cell(row=row, column=cant_var).value
    ID_anterior = None
    while ID:
        datos_factura = []
        if ID != ID_anterior:
            #ID
            #tipo_factura_nota
            #nombre_apellido_cliente
            #tipo_documento
            #nro_doc_cliente
            #condicion_venta_cliente
            #condicion_IVA_cliente
            #concepto_producto_servicio
            #fecha_ser_desde
            #fecha_ser_hasta
            #fecha_vencimiento_pago
            while cant_var < 12:
                datos_factura.append(factura_hoja.cell(row=row, column=cant_var).value)
                cant_var+=1
            
            productos_servicios = []
            tributos = []
            obtener_productos_servicios(excel_dataframe, datos_factura, row, productos_servicios, tributos)
            datos_factura.append(productos_servicios)
            datos_factura.append(tributos)
            factura_hoja=excel_dataframe["Facturas_A_Realizar"]
            ID_anterior = ID
        datos_facturas_total.append(datos_factura)
        cant_var = 1
        row += 1
        ID = factura_hoja.cell(row=row, column=1).value

    return datos_facturas_total