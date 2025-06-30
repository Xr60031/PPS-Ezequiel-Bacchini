import json
from impresor_pdf.strategies.facturaC import Factura_C
from impresor_pdf.strategies.notaCredito import Nota_Credito
import urllib.parse

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
		Identificador_factura = datos_CAE[2]
		nombre_apellido_cliente =  datos_factura["Nombre_y_Apellido_Cliente"]
		importe_total = datos_factura["Importe_Total"]
		producto_servicio = datos_factura["items"]
		nombre_facturante = biblioteca_datos_vendedor["Nombre"]
		cuit_facturante = biblioteca_datos_vendedor["CUIT"]
		nombre_fantasia_facturante = biblioteca_datos_vendedor["Nombre_Empresa"]
		punto_venta = biblioteca_datos_vendedor["Punto_de_venta"]
		razon_social_facturante = biblioteca_datos_vendedor["Razon_Social"]
		domicilio_comercial_facturante = biblioteca_datos_vendedor["Domicilio"]
		condicion_iva_facturante = biblioteca_datos_vendedor["Condicion_frente_al_IVA"]
		ingresos_brutos_facturante = biblioteca_datos_vendedor["Ingresos_Brutos"]
		fecha_inicio_actividad_facturante = biblioteca_datos_vendedor["Fecha_Inicio"]
		condicion_venta_cliente = datos_factura["Condicion_de_venta_Cliente"]
		condicion_iva_cliente = datos_factura["Condicion_frente_al_IVA_Cliente"]
		cant_de_productos_servicios = len(datos_factura["items"])
		fecha_limite_factura = datos_factura["Fecha_vencimiento_de_pago"]
		importe_otros_tributos = datos_factura["Importe_Tributo"]
		n_cae = datos_CAE[0]
		fecha_vto_cae = datos_CAE[1]
		tipo_factura_nota = datos_factura["ID_factura_nota"]
		fecha_desde = datos_factura["Fecha_servicio_desde"]
		tipo_documento_cliente = datos_factura["Tipo_Documento"]
		numero_documento_cliente = datos_factura["Numero_de_documento_del_cliente"]
		fecha_hasta = datos_factura["Fecha_servicio_hasta"]
		fecha_emision = datos_factura["fecha_emision"]

		qr_content = self.hacer_JSON(
			fecha_emision,
			cuit_facturante,
			punto_venta,
			tipo_factura_nota,
			importe_total,
			"PES",
			1.00,
			tipo_documento_cliente,
			numero_documento_cliente,
			n_cae
			)
		
		strategy = None
		
		if  tipo_factura_nota == 11:
			strategy = Factura_C()
		elif tipo_factura_nota == 13:
			strategy = Nota_Credito()
		
		if strategy == None:
			return
		
		return strategy.generar_pdf(
			Identificador_factura,
			nombre_apellido_cliente,
			importe_total,
			producto_servicio,
			nombre_facturante,
			cuit_facturante,
			nombre_fantasia_facturante,
			punto_venta,
			razon_social_facturante,
			domicilio_comercial_facturante,
			condicion_iva_facturante,
			ingresos_brutos_facturante,
			fecha_inicio_actividad_facturante,
			condicion_venta_cliente,
			condicion_iva_cliente,
			cant_de_productos_servicios,
			fecha_limite_factura,
			importe_otros_tributos,
			n_cae,
			fecha_vto_cae,
			fecha_desde,
			fecha_hasta,
			qr_content,
			fecha_emision
			)