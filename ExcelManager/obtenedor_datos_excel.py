from Constantes.Excel.constantes_excel import constantes_posicion_datos_factura_excel, constantes_genericas_excel, constantes_posicion_items_excel
from Constantes.Facturacion.constantes_arrays import constantes_obtenedor_datos
class Obtenedor_Datos_Excel():
    def __init__(self):
        self

    def obtener_datos_hoja_factura_item_actual(self, factura_hoja, row):
        cantidad = float(factura_hoja.cell(row=row, column=constantes_posicion_datos_factura_excel.pos_Cantidad.value).value or 0)
        porcentaje_bonificado = factura_hoja.cell(row=row, column=constantes_posicion_datos_factura_excel.pos_Porcentaje_bonificado.value).value
        nombre_producto_servicio = factura_hoja.cell(row=row, column=constantes_posicion_datos_factura_excel.pos_Producto_Servicio.value).value

        datos_hoja_factura = [
            int(cantidad),                  #Cantidad
            porcentaje_bonificado or 0,     #Porcentaje Bonificado
            nombre_producto_servicio        #Nombre Producto/Servicio
        ]
        return datos_hoja_factura

    def obtener_datos_hoja_item_actual(self, items, datos_hoja_factura):
        row_ = constantes_genericas_excel.starting_row.value
        while items.cell(row=row_, column=constantes_genericas_excel.starting_colvar.value).value and datos_hoja_factura[constantes_obtenedor_datos.pos_nombre_producto_servicio.value] != items.cell(row=row_, column=constantes_genericas_excel.starting_colvar.value).value:
            row_ += 1

        codigo_producto = items.cell(row=row_, column=constantes_posicion_items_excel.pos_Codigo.value).value
        descripcion = items.cell(row=row_, column=constantes_posicion_items_excel.pos_Descripcion.value).value
        precio_unitario = float(items.cell(row=row_, column=constantes_posicion_items_excel.pos_Precio_Unitario.value).value or 0)
        impuesto_adicional = items.cell(row=row_, column=constantes_posicion_items_excel.pos_Impuesto_Adicional.value).value
        descripcion_tributo_adicional = items.cell(row=row_, column=constantes_posicion_items_excel.pos_Descripcion_Impuesto.value).value
        alicuota = float(items.cell(row=row_, column=constantes_posicion_items_excel.pos_Alicuota.value).value or 0)
        
        importe_bonificado = 0
        subtotal = 0

        datos_hoja_item = [
            codigo_producto,
            descripcion,
            precio_unitario,
            impuesto_adicional,
            descripcion_tributo_adicional,
            alicuota,
            importe_bonificado,
            subtotal
        ]

        return datos_hoja_item