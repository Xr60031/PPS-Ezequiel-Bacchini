from impresor_pdf.templates.template import Template

class Factura_B(Template):
    def __init__(self, tipo_factura_nota, codigo_tipo_factura_nota, factura_nota):
        super().__init__(tipo_factura_nota, codigo_tipo_factura_nota, factura_nota)

    def armar_datos_usuario_opcionales(self, biblioteca_datos_vendedor, datos_CAE, datos_factura):
        pass

    def unir_datos_usuario(self, datos_comunes, datos_opcionales):
        return datos_comunes

    def armar_datos_cliente_opcionales(self, datos_factura):
        datos_cliente_opcionales = [
            f'Nombre y apellido: {datos_factura["Nombre_y_Apellido_Cliente"]}',
            f'Domicilio: {datos_factura["Direccion"]}'
        ]
        return datos_cliente_opcionales
    
    def unir_datos_cliente(self, datos_comunes, datos_opcionales):
        datos_unidos = []
        datos_unidos.extend(datos_comunes)
        datos_unidos.extend(datos_opcionales)
        return datos_unidos
    
    def armar_titulos_items_opcionales(self):
        pass

    def unir_titulos_items(self, titulos_comunes, titulos_opcional):
        return titulos_comunes
    
    def armar_items_opcionales(self, datos_factura):
        pass
    
    def unir_items(self, items_comunes, items_opcionales):
        return items_comunes

    def armar_subtotales_opcionales(self, datos_factura):
        pass

    def unir_subtotales(self, subtotales_comunes, subtotales_opcionales):
        return subtotales_comunes