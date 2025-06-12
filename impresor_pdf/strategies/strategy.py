from abc import ABC, abstractmethod

class Strategy(ABC):
    def __init__(self):
        super().__init__()
        self.no_aplica = "No Aplica"

    @abstractmethod
    def generar_pdf(self,
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
    ):
        pass

    def hacer_Linea(self, pdf):
        pdf.line(pdf.get_x(), pdf.get_y(), pdf.w-10, pdf.get_y())
