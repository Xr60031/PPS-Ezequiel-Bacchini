from Constantes.ARCA.constantes_ids_ARCA import ID_Concepto, ID_Condicion_IVA_Cliente, ID_Documento, ID_Factura, ID_Tributo, ID_Nota_Credito
class Obtenedor_ID():
    def __init__(self):
        self

    def obtener_ID_tributo(self, impuesto):
        return{
            'Impuestos Nacionales' : ID_Tributo.IMPUESTOS_NACIONALES.value,
            'Impuestos Provinciales' : ID_Tributo.IMPUESTOS_PROVINCIALES.value,
            'Tributos Municipales' : ID_Tributo.TRIBUTOS_MUNICIPALES.value,
            'Impuestos Internos' : ID_Tributo.IMPUESTOS_INTERNOS.value,
            'IIBB' : ID_Tributo.IIBB.value,
            'Percepción de IVA' : ID_Tributo.PERCEPCION_DE_IVA.value,
            'Percepción de IIBB' : ID_Tributo.PERCEPCION_DE_IIBB.value,
            'Percepciones por Tributos Municipales' : ID_Tributo.TRIBUTOS_MUNICIPALES.value,
            'Otras Percepciones' : ID_Tributo.OTRAS_PERCEPCIONES.value,
            'Percepción de IVA a no Categorizado' : ID_Tributo.PERCEPCION_DE_IVA_NO_CATEGORIZADO.value,
            'Otros' : ID_Tributo.OTROS.value,
        }.get(impuesto)

    def obtener_ID_documento(self, documento):
        return{
            'CONSUMIDOR FINAL' : ID_Documento.CONSUMIDOR_FINAL.value,
            'CUIT' : ID_Documento.CUIT.value,
            'CDI' : ID_Documento.CDI.value,
            'CI EXTRANJERA' : ID_Documento.CI_EXTRANJERA.value,
            'PASAPORTE' : ID_Documento.PASAPORTE.value,
            'DNI' : ID_Documento.DNI.value
        }.get(documento)

    def obtener_ID_concepto(self, concepto):
        return{
            'PRODUCTOS' : ID_Concepto.PRODUCTOS.value,
            'SERVICIOS' : ID_Concepto.SERVICIOS.value,
            'PRODUCTOS Y SERVICIOS' : ID_Concepto.PRODUCTOS_Y_SERVICIOS.value
        }.get(concepto)

    def obtener_ID_Factura(self, tipo_factura):
        return{
            'Factura C' : ID_Factura.FACTURA_C.value,
            'Factura A' : ID_Factura.FACTURA_A.value,
            'Factura B' : ID_Factura.FACTURA_B.value
        }.get(tipo_factura)
    
    def obtener_ID_Nota(self, tipo_factura):
        return{
            'Factura C' : ID_Nota_Credito.NOTA_C.value,
            'Factura A' : ID_Nota_Credito.NOTA_A.value,
            'Factura B' : ID_Nota_Credito.NOTA_B.value
        }.get(tipo_factura)

    def obtener_ID_condicion_iva_cliente(self, tipo_iva):
        return{
            'Consumidor Final': ID_Condicion_IVA_Cliente.CONSUMIDOR_FINAL.value,
            'Monotributista' : ID_Condicion_IVA_Cliente.MONOTRIBUTISTA.value,
            'Excento' : ID_Condicion_IVA_Cliente.EXCENTO.value,
            'Responsable Inscripto': ID_Condicion_IVA_Cliente.RESPONSABLE_INSCRIPTO.value,
        }.get(tipo_iva)