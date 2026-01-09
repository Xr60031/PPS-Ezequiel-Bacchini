import json
from impresor_pdf.templates.facturaC import Factura_C
from impresor_pdf.templates.notaCreditoC import Nota_Credito_C
from impresor_pdf.templates.facturaA import Factura_A
from impresor_pdf.templates.notaCreditoA import Nota_Credito_A
from impresor_pdf.templates.facturaB import Factura_B
from impresor_pdf.templates.notaCreditoB import Nota_Credito_B

import urllib.parse
from Constantes.ARCA.constantes_ids_ARCA import ID_Factura, ID_Nota_Credito
class Impresor_PDF():
	def __init__(self):
		self

	def formatear_fecha_emision_str(self, fecha_str):
		mes, dia, anio = fecha_str.split("-")
		return f"{anio}{mes.zfill(2)}{dia.zfill(2)}"

	def hacer_JSON(self,
		fecha_desde,
		cuit,
		punto_venta,
		tipo_comprobante,
		importe,
		moneda,
		cotizacion,
		tipo_documento,
		numero_documento,
		cae
	):
		data = {
		"ver": 1,
		"fecha": str(fecha_desde),
		"cuit": cuit,
		"ptoVta": punto_venta,
		"tipoCmp": tipo_comprobante,
		"importe": float(importe),
		"moneda": moneda,
		"ctz": float(cotizacion),
		"tipoDocRec": tipo_documento,
		"nroDocRec": numero_documento,
		"tipoCodAut": "E",
		"codAut": int(cae)
		}

		json_str = json.dumps(data, separators=(',', ':'))
		json_encoded = urllib.parse.quote(json_str, safe='')
		qr_url = f"https://www.afip.gob.ar/fe/qr/?p={json_encoded}"
		return qr_url

	def generar_pdf_(self,
		datos_factura,
		biblioteca_datos_vendedor,
		datos_CAE
		):

		qr_content = self.hacer_JSON(
			datos_factura["fecha_emision"],
			biblioteca_datos_vendedor["CUIT"],
			biblioteca_datos_vendedor["Punto_de_venta"],
			datos_factura["ID_factura_nota"],
			datos_factura["Importe_Total"],
			"PES",
			1.00,
			datos_factura["Tipo_Documento"],
			datos_factura["Numero_de_documento_del_cliente"],
			datos_CAE[0]
			)
		
		template = None
		
		if  datos_factura["ID_factura_nota"] == ID_Factura.FACTURA_C.value:
			template = Factura_C("C", "N 11", "Factura")
		elif datos_factura["ID_factura_nota"] == ID_Nota_Credito.NOTA_C.value:
			template = Nota_Credito_C("C", "N 13", "Nota de Crédito")
		elif datos_factura["ID_factura_nota"] == ID_Factura.FACTURA_A.value:
			template = Factura_A("A", "N 1", "Factura")
		elif datos_factura["ID_factura_nota"] == ID_Nota_Credito.NOTA_A.value:
			template = Nota_Credito_A("A", "N 3", "Nota de Crédito")
		elif datos_factura["ID_factura_nota"] == ID_Factura.FACTURA_B.value:
			template = Factura_B("B", "N 6", "Factura")
		elif datos_factura["ID_factura_nota"] == ID_Nota_Credito.NOTA_B.value:
			template = Nota_Credito_B("B", "N 8", "Nota de Crédito")


		if template == None:
			return
		
		return template.generar_pdf(
			datos_factura,
			biblioteca_datos_vendedor,
			datos_CAE,
			qr_content,
			f'temp_{biblioteca_datos_vendedor["CUIT"]}_qr.png' #qr filename
			)