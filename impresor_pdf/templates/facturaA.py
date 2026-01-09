from impresor_pdf.templates.template import Template
from impresor_pdf.templates.enums import X_pos

class Factura_A(Template):
    def __init__(self, tipo_factura_nota, codigo_tipo_factura_nota, factura_nota):
        super().__init__(tipo_factura_nota, codigo_tipo_factura_nota, factura_nota)

    def armar_datos_usuario_opcionales(self, biblioteca_datos_vendedor, datos_CAE, datos_factura):
        pass

    def unir_datos_usuario(self, datos_comunes, datos_opcionales):
        return datos_comunes

    def armar_datos_cliente_opcionales(self, datos_factura):
        datos_opcionales =[
            f'Domicilio: {datos_factura["Direccion"]}',
            f'Localidad: {datos_factura["Localidad"]}',
            f'Provincia: {datos_factura["Provincia"]}',
            f'Telefono: {datos_factura["Telefono"]}'
        ]
        return datos_opcionales
    
    def unir_datos_cliente(self, datos_comunes, datos_opcionales):
        datos_unidos = []
        datos_unidos.extend(datos_comunes),
        datos_unidos.extend(datos_opcionales)
        return datos_unidos
    
    def armar_titulos_items_opcionales(self):
        titulos_adicionales = [
            [   X_pos.SUBTOTAL.value, 
                40, 
                'Importe:'],
            [   X_pos.ALIC_IVA.value, 
                20, 
                'IVA %:'
            ]
        ]
        return titulos_adicionales

    def unir_titulos_items(self, titulos_comunes, titulos_opcional):
        titulos_unidos = []
        titulos_unidos.extend(titulos_comunes)
        titulos_unidos.pop()
        titulos_unidos.extend(titulos_opcional)
        return titulos_unidos
    
    def armar_items_opcionales(self, datos_factura):
        datos_adicionales = []
        for cant in range(len(datos_factura["items"])):
            item_actual = []
            item_actual.extend([
                [
                    X_pos.SUBTOTAL.value,
                    20,
                    str(datos_factura["items"][cant][9])
                ]
            ])

            datos_adicionales.append(item_actual)
        return datos_adicionales
    
    def unir_items(self, items_comunes, items_opcionales):
        items_unificados = []
        for cant in range(len(items_comunes)):
            item_actual = []
            item_actual.extend(items_comunes[cant])
            item_actual.extend(items_opcionales[cant])
            items_unificados.append(item_actual)
        return items_unificados
        

    def armar_subtotales_opcionales(self, datos_factura):
        subtotales_adicionales = [
            f'Importe Neto Gravado: {int((datos_factura["Importe_Total"]-datos_factura["Importe_Tributo"])*100)/100}',
            f'IVA 21%: {datos_factura["Importe_IVA_21%"]}',
            f'IVA 10,5%: {datos_factura["Importe_IVA_10.5%"]}'
        ]
        return subtotales_adicionales
        

    def unir_subtotales(self, subtotales_comunes, subtotales_opcionales):
        subtotales_comunes_temp = []
        subtotales_comunes_temp.extend(subtotales_comunes)
        subtotales_comunes_temp.pop()

        subtotales_unidos = []
        subtotales_unidos.extend(subtotales_opcionales)
        subtotales_unidos.extend(subtotales_comunes_temp)
        return subtotales_unidos