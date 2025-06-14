from openpyxl import load_workbook
from Funciones.biblioteca_factura import armar_biblioteca_factura
from ExcelManager.obtener_datos_hoja_factura_actual import obtener_datos_hoja_factura_item_actual
from ExcelManager.obtener_datos_hoja_item_actual import obtener_datos_hoja_item_actual
from Funciones.armar_item import armar_datos_producto_servicio

def obtener_ID(factura_hoja, row):
    return factura_hoja.cell(row=row, column=1).value

def obtener_productos_servicios(excel_dataframe, datos_factura, biblioteca_datos_vendedor, row): 
    ID = datos_factura["Identificador_Factura"]
    ID_anterior = ID
    i=0
    imp_neto=0
    imp_total=0
    imp_total = float(imp_total)
    imp_tributo=0
    productos_servicios = []
    tributos = []
    hoja_actual = excel_dataframe["Facturas_A_Realizar"]

    while ID == ID_anterior and ID != "" :
        datos_hoja_factura = obtener_datos_hoja_factura_item_actual(hoja_actual, row)
        hoja_actual = excel_dataframe["Items"]
        datos_hoja_item = obtener_datos_hoja_item_actual(hoja_actual, datos_hoja_factura)
        armar_datos_producto_servicio(productos_servicios, tributos, datos_hoja_factura, datos_hoja_item)
        # + subtotal
        imp_total += productos_servicios[i][8]
        # + importe_bonificado
        imp_neto += productos_servicios[i][7]
        
        ID_anterior = ID
        i += 1
        row += 1
        hoja_actual = excel_dataframe["Facturas_A_Realizar"]
        ID = obtener_ID(hoja_actual, row) 

    if biblioteca_datos_vendedor["id_tributo_global"]:
        tributos.append([
            #ID_tributo
            biblioteca_datos_vendedor["id_tributo_global"],
            #descripcion_impuesto_adicional
            biblioteca_datos_vendedor["desc_iag"],
            #imp_neto
            imp_neto,
            #alicuota_impuesto_adicional
            biblioteca_datos_vendedor["alicuota"],
            #imp_neto*alicuota_impuesto_adicional
            imp_neto*(biblioteca_datos_vendedor["alicuota"] or 0)/100
        ])
        imp_total += imp_neto*(biblioteca_datos_vendedor["alicuota"] or 0)/100

    datos_factura["tributos"] = tributos
    if len(datos_factura["tributos"]) == 0:
        datos_factura["Importe_Tributo"] = 0
    else:
        imp_tributo = imp_total - imp_neto
        datos_factura["Importe_Tributo"] = imp_tributo

    datos_factura["Importe_Total"] = imp_total
    datos_factura["Importe_Neto"] = imp_neto
    datos_factura["tributos"] = tributos
    datos_factura["items"] = productos_servicios

#Abre la plantilla de excel y devuelve una lista con todos los datos que el sistema necesita para facturar
def obtener_datos_factura(filename, biblioteca_datos_vendedor):
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

            
            biblioteca_factura = armar_biblioteca_factura(datos_factura)
            obtener_productos_servicios(excel_dataframe, biblioteca_factura, biblioteca_datos_vendedor, row)
            factura_hoja=excel_dataframe["Facturas_A_Realizar"]
            ID_anterior = ID
        datos_facturas_total.append(biblioteca_factura)
        cant_var = 1
        row += 1
        ID = factura_hoja.cell(row=row, column=1).value

    return datos_facturas_total