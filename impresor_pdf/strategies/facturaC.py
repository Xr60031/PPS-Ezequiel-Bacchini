from impresor_pdf.strategies.strategy import Strategy
from fpdf import FPDF
import os
import segno
import math
from io import BytesIO

class Factura_C(Strategy):
    def __init__(self):
        super().__init__()
    
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
    fecha_emision):
        
        pdf = FPDF()
        pdf.add_page()
        identacion = 5
        identacion_grande = 15

        tipo_factura="C"
        codigo_tipo_factura="N 11"
        iteracion = 1
        while iteracion < 3:
            pdf.rect(5, 5, 200, 287)

            pdf.set_font('Arial', style="B", size=20)

            pdf.set_xy(10,10)
            
            self.hacer_Linea(pdf)
            if(iteracion == 1):
                pdf.cell(0,10, 'ORIGINAL', ln=True, align='C')
            else:
                pdf.cell(0,10, 'DUPLICADO', ln=True, align='C')
            self.hacer_Linea(pdf)

            x_start = 94.5
            y_start = pdf.get_y()
            line_height = 10 
            num_lines = 7
            y_end = y_start + (line_height * num_lines)
            pdf.set_draw_color(0, 0, 0)
            pdf.line(x_start, y_start, x_start, y_end)


            pdf.set_font('Arial', style="B", size=20)
            pdf.cell(0,identacion_grande, nombre_fantasia_facturante, align='L')
            pdf.cell(0,identacion_grande, 'FACTURA', ln=True, align='R')

            pdf.set_font('Arial', style="B", size=10)
            pdf.cell(0,identacion+2, F'Razón Social: {razon_social_facturante}', align='L')
            pdf.cell(0,identacion+2, F'Punto de Venta: {punto_venta}', ln=True, align='R')
            pdf.cell(0,identacion+2, F'Domicilio Comercial: {domicilio_comercial_facturante}', align='L')
            pdf.cell(0,identacion+2, F'Comp. Nro: {int(Identificador_factura)}', ln=True, align='R')
            pdf.cell(0,identacion+2, F'Condición Frente al IVA: {condicion_iva_facturante}', align='L')
            pdf.cell(0,identacion+2, F'Fecha de Emisión: {fecha_emision}', ln=True, align='R')
            pdf.cell(0,identacion+2, F'Cuit: {cuit_facturante}', ln=True, align='R')
            pdf.cell(0,identacion+2, F'Ingresos Brutos: {ingresos_brutos_facturante}', ln=True, align='R')
            pdf.cell(0,identacion+2, F'Fecha de Inicio de Actividades: {fecha_inicio_actividad_facturante}', ln=True, align='R')

            pdf.set_font('Arial', style="B", size=15)

            texto_completo = F'{tipo_factura}\nCódigo: {codigo_tipo_factura}'

            ancho_texto = pdf.get_string_width(texto_completo)
            ancho_celda = ancho_texto + 6

            x_centrada = (pdf.w - 20) / 2
            y_inicial = 20

            pdf.set_xy(x_centrada, y_inicial)

            pdf.multi_cell(ancho_celda, identacion, texto_completo, border=1, align='C')

            pdf.set_draw_color(0, 0, 0)
            pdf.line(x_centrada, y_inicial, x_centrada + ancho_celda, y_inicial)
            pdf.line(x_centrada, y_inicial + 10, x_centrada + ancho_celda, y_inicial + 10)
            pdf.line(x_centrada, y_inicial, x_centrada, y_inicial + 10)
            pdf.line(x_centrada + ancho_celda, y_inicial, x_centrada + ancho_celda, y_inicial + 10)

            pdf.set_y(y_inicial + 20)

            pdf.ln(50)
            pdf.set_font('Arial', style="B", size=10)
            ancho_fecha_desde = pdf.get_string_width(f'Período Facturado Desde: {fecha_desde or self.no_aplica}')
            ancho_fecha_hasta = pdf.get_string_width(f'Hasta: {fecha_hasta or self.no_aplica}') + 50
            ancho_fecha_limite = pdf.get_string_width(f'Fecha de Vto. para el pago: {fecha_limite_factura or self.no_aplica}')

            self.hacer_Linea(pdf)
            pdf.set_font('Arial', style="B", size=10)
            pdf.cell(ancho_fecha_desde,10, F'Período Facturado Desde: {fecha_desde or self.no_aplica}', align='C')
            pdf.set_x(pdf.get_x() - 13)
            pdf.cell(ancho_fecha_hasta,10, F'Hasta: {fecha_hasta or self.no_aplica}', align='C')
            pdf.set_x(pdf.get_x() - 15)
            pdf.cell(ancho_fecha_limite,10, F'Fecha de Vto. para el pago: {fecha_limite_factura or self.no_aplica}', ln=True, align='C')
            self.hacer_Linea(pdf)

            pdf.ln(1)

            self.hacer_Linea(pdf)
            pdf.cell(0,identacion, F'Apellido y Nombre / Razón Social: {nombre_apellido_cliente}', ln=True, align='L')
            pdf.cell(0,identacion, F'Condicion frente al IVA: {condicion_iva_cliente}', ln=True, align='L')
            pdf.cell(0,identacion, F'Condicion de Venta: {condicion_venta_cliente}', ln=True, align='L')
            self.hacer_Linea(pdf)

            pdf.ln(1)

            self.hacer_Linea(pdf)
            pdf.set_font('Arial', style="B", size=10)

            x_codigo = 10
            pdf.set_x(x_codigo)
            pdf.cell(20 ,identacion, 'Código:', align='L')

            x_producto_servicio = x_codigo + 20
            pdf.set_x(x_producto_servicio)
            pdf.cell(60,identacion, 'Producto/Servicio:', align='L')


            x_cantidad = x_producto_servicio + 50
            pdf.set_x(x_cantidad)
            pdf.cell(20,identacion, 'Cantidad:', align='L')


            x_precio_unitario = x_cantidad + 20
            pdf.set_x(x_precio_unitario)
            pdf.cell(10,identacion, 'Precio Unitario:', align='L')

            x_bonif_porcentaje = x_precio_unitario + 30
            pdf.set_x(x_bonif_porcentaje)
            pdf.cell(10,identacion, '% Bonif:', align='L')

            x_imp_bonif = x_bonif_porcentaje + 20
            pdf.set_x(x_imp_bonif)
            pdf.cell(10, identacion, 'Imp. Bonif:', align='L')

            x_subtotal = x_imp_bonif + 25
            pdf.set_x(x_subtotal)
            pdf.cell(40, identacion, 'Subtotal:', ln=True, align='L')
            
            self.hacer_Linea(pdf)

            pdf.ln(1)
            
            self.hacer_Linea(pdf)
            pdf.set_font('Arial', size=8)
            

            for i in range(math.ceil(cant_de_productos_servicios/24)-1):
                pdf.add_page()
                pdf.rect(5, 5, 200, 287)
                pdf.set_font('Arial', style="B", size=8)

            for cant in range(cant_de_productos_servicios):
                pdf.set_x(x_codigo)
                pdf.cell(40,5, str(producto_servicio[cant][3]), align='L')
                
                pdf.set_x(x_producto_servicio)
                pdf.cell(20,5, str(producto_servicio[cant][0]), align='L') #Producto/Serivcio

                pdf.set_x(x_cantidad)
                pdf.cell(20,5, str(int(producto_servicio[cant][2])), align='L')

                pdf.set_x(x_precio_unitario)
                pdf.cell(20,5, str(producto_servicio[cant][5]), align='L')

                pdf.set_x(x_bonif_porcentaje)
                pdf.cell(30,5, str(producto_servicio[cant][1]), align='L')

                pdf.set_x(x_imp_bonif)
                pdf.cell(20,5, str(producto_servicio[cant][7]), align='L')

                pdf.set_x(x_subtotal)
                pdf.cell(20,5, str(producto_servicio[cant][8]), ln=True, align='L')

            self.hacer_Linea(pdf)

            pdf.set_font('Arial', style="B", size=10)
            pdf.cell(0,identacion, F'Subtotal:$ {int((importe_total-importe_otros_tributos)*100)/100}', ln=True, align='R')
            pdf.cell(0,identacion, F'Importe Otros Tributos:$ {importe_otros_tributos}', ln=True, align='R')
            pdf.cell(0,identacion, F'Total:$ {importe_total}', ln=True, align='R')
            
            self.hacer_Linea(pdf)

            pdf.ln(1)

            pdf.set_font('Arial', style="B", size=10)
            pdf.cell(0, identacion, F'CAE N.: {n_cae}', ln=True, align='R')
            pdf.cell(0, identacion, F'Fecha de Vto. de CAE: {fecha_vto_cae}', ln=True, align='R')


            #Genero el QR en memoria
            qr_buffer = segno.make(qr_content)
            qr_buffer_io = BytesIO()
            qr_buffer.save(qr_buffer_io, kind="png", scale=5)
            qr_buffer_io.seek(0)

            qr_filename = f'temp_{cuit_facturante}_qr.png'

            with open(qr_filename,"wb") as f:
                f.write(qr_buffer_io.getvalue())

            qr_x = 10
            qr_y = 265
            qr_size = 25

            pdf.image(qr_filename, x=qr_x, y=qr_y, w=qr_size, h=qr_size)
            pdf.set_auto_page_break(auto=True, margin=5)

            image_x = qr_x  + qr_size + 6
            image_y = qr_y 
            image_w = 50  # Ancho de la imagen
            image_h = 15  # Alto de la imagen

            pdf.image('impresor_pdf/Arca_logo.jpg', x=image_x, y=image_y, w=image_w, h=image_h)

            text_x = qr_x + qr_size + 5
            text_y = qr_y
            pdf.set_xy(text_x, text_y + 15)
            pdf.set_font('Arial', style="B", size=8)
            pdf.cell(0, identacion, 'Comprobante Autorizado', ln=True, align='L')

            pdf.set_xy(text_x, text_y + 20) 
            pdf.set_font('Arial', size=6)
            pdf.cell(0, identacion, 'Esta Administración Federal no se responsabiliza por los datos ingresados en el detalle de la operación', ln=True, align='L')
            
            if(iteracion == 1):
                pdf.add_page()
            iteracion += 1
        
        os.remove(qr_filename)

        answer = []
        answer.append(Identificador_factura)
        answer.append(pdf.output(dest='S').encode('latin1'))
        return answer