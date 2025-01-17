import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from fpdf import FPDF
from datetime import datetime

def hacer_Linea(pdf):
    pdf.line(pdf.get_x(), pdf.get_y(), pdf.w-10, pdf.get_y())

def generar_factura():
    tipo_factura="N/A"
    codigo_tipo_factura=0

    nombre_apellido_cliente="NOMBRE"
    condicion_venta_cliente="N/A"
    condicion_iva_cliente="N/A"

    nombre_fantasia_facturante="N/A"
    razon_social_facturante="N/A"
    domicilio_comercial_facturante="N/A"
    condicion_iva_facturante="N/A"
    ingresos_brutos_facturante=0
    cuit_facturante=0
    fecha_inicio_actividad_facturante=0

    punto_venta=0
    numero_compra=0

    fecha_emision_factura = datetime.now().strftime('%d/%m/%y')
    fecha_limite_factura=0

    codigo_prod_ser=100000
    prod_ser=0
    cantidad_prod_ser=0
    precio_unidad=0
    por_bonificado=0
    imp_bonificado=0
    importe_subtotal=0

    importe_otros_tributos=0
    importe_total=0

    n_cae=0
    fecha_vto_cae=0

    pdf = FPDF()
    pdf.add_page()

    pdf.rect(5, 5, 200, 287)

    logo_path = 'logo.png'

    pdf.image(logo_path, x=(pdf.w - 20) / 2 - 21, y=21, w=20, h=20)

    pdf.set_font('Arial', style="B", size=20)

    pdf.set_xy(10,10)
    
    hacer_Linea(pdf)
    pdf.cell(0,10, 'ORIGINAL', ln=True, align='C')
    hacer_Linea(pdf)

    x_start = 94.5
    y_start = pdf.get_y()
    line_height = 10 
    num_lines = 7
    y_end = y_start + (line_height * num_lines)
    pdf.set_draw_color(0, 0, 0)
    pdf.line(x_start, y_start, x_start, y_end)


    pdf.set_font('Arial', style="B", size=20)
    pdf.cell(0,10, nombre_fantasia_facturante, align='L')
    pdf.cell(0,10, 'FACTURA', ln=True, align='R')

    pdf.set_font('Arial', style="B", size=10)
    pdf.cell(0,10, F'Razón Social: {razon_social_facturante}', align='L')
    pdf.cell(0,10, F'Punto de Venta: {punto_venta}', ln=True, align='R')
    pdf.cell(0,10, F'Domicilio Comercial: {domicilio_comercial_facturante}', align='L')
    pdf.cell(0,10, F'Comp. Nro: {numero_compra}', ln=True, align='R')
    pdf.cell(0,10, F'Condición Frente al IVA: {condicion_iva_facturante}', align='L')
    pdf.cell(0,10, F'Fecha de Emisión: {fecha_emision_factura}', ln=True, align='R')
    pdf.cell(0,10, F'Cuit: {cuit_facturante}', ln=True, align='R')
    pdf.cell(0,10, F'Ingresos Brutos: {ingresos_brutos_facturante}', ln=True, align='R')
    pdf.cell(0,10, F'Fecha de Inicio de Actividades: {fecha_inicio_actividad_facturante}', ln=True, align='R')

    pdf.set_font('Arial', style="B", size=10)

    texto_completo = F'{tipo_factura}\nCódigo: {codigo_tipo_factura}'

    ancho_texto = pdf.get_string_width(texto_completo)
    ancho_celda = ancho_texto + 6

    x_centrada = (pdf.w - 20) / 2
    y_inicial = 20

    pdf.set_xy(x_centrada, y_inicial)

    pdf.multi_cell(ancho_celda, 10, texto_completo, border=1, align='C')

    pdf.set_draw_color(0, 0, 0)
    pdf.line(x_centrada, y_inicial, x_centrada + ancho_celda, y_inicial)
    pdf.line(x_centrada, y_inicial + 20, x_centrada + ancho_celda, y_inicial + 20)
    pdf.line(x_centrada, y_inicial, x_centrada, y_inicial + 20)
    pdf.line(x_centrada + ancho_celda, y_inicial, x_centrada + ancho_celda, y_inicial + 20)

    pdf.set_y(y_inicial + 20)

    pdf.ln(50)
    
    ancho_fecha_emision = pdf.get_string_width(f'Período Facturado Desde: {fecha_emision_factura}')
    ancho_fecha_hasta = pdf.get_string_width(f'Hasta: {fecha_limite_factura}') + 50
    ancho_fecha_limite = pdf.get_string_width(f'Fecha de Vto. para el pago: {fecha_limite_factura}')

    hacer_Linea(pdf)
    pdf.set_font('Arial', style="B", size=10)
    pdf.cell(ancho_fecha_emision,10, F'Período Facturado Desde: {fecha_emision_factura}', align='C')
    pdf.cell(ancho_fecha_hasta,10, F'Hasta: {fecha_limite_factura}', align='C')
    pdf.cell(ancho_fecha_limite,10, F'Fecha de Vto. para el pago: {fecha_limite_factura}', ln=True, align='C')
    hacer_Linea(pdf)

    pdf.ln(1)

    hacer_Linea(pdf)
    pdf.cell(0,10, F'Apellido y Nombre / Razón Social: {nombre_apellido_cliente}', ln=True, align='L')
    pdf.cell(0,10, F'Condicion frente al IVA: {condicion_iva_cliente}', ln=True, align='L')
    pdf.cell(0,10, F'Condicion de Venta: {condicion_venta_cliente}', ln=True, align='L')
    hacer_Linea(pdf)

    pdf.ln(1)

    espacio=10

    ancho_codigo = pdf.get_string_width('Código:') + espacio
    ancho_prod_ser = pdf.get_string_width('Producto/Servicio:') + espacio
    ancho_cant = pdf.get_string_width('Código:') + espacio
    ancho_precio_unitario=pdf.get_string_width('Precio Unitario:') + espacio
    ancho_bonif_por=pdf.get_string_width('% Bonif:') + espacio
    ancho_bonif_imp=pdf.get_string_width('Imp. Bonif:') + espacio
    ancho_subtotal=pdf.get_string_width('Subtotal:') + espacio

    hacer_Linea(pdf)
    pdf.cell(ancho_codigo,10, 'Código:', align='L')
    pdf.cell(ancho_prod_ser,10, 'Producto/Servicio:', align='L')
    pdf.cell(ancho_cant,10, 'Cantidad:', align='L')
    pdf.cell(ancho_precio_unitario,10, 'Precio Unitario:', align='L')
    pdf.cell(ancho_bonif_por,10, '% Bonif:', align='L')
    pdf.cell(ancho_bonif_imp,10, 'Imp. Bonif:', align='L')
    pdf.cell(ancho_subtotal,10, 'Subtotal:', ln=True, align='L')
    hacer_Linea(pdf)

    pdf.ln(1)

    hacer_Linea(pdf)
    pdf.set_font('Arial', size=10)
    pdf.cell(ancho_codigo,10, str(codigo_prod_ser), align='L')
    pdf.cell(ancho_prod_ser,10, str(prod_ser), align='L')
    pdf.cell(ancho_cant,10, str(cantidad_prod_ser), align='L')
    pdf.cell(ancho_precio_unitario,10, str(precio_unidad), align='L')
    pdf.cell(ancho_bonif_por,10, str(por_bonificado), align='L')
    pdf.cell(ancho_bonif_imp,10, str(imp_bonificado), align='L')
    pdf.cell(ancho_subtotal,10, str(importe_subtotal), ln=True, align='L')
    hacer_Linea(pdf)

    pdf.ln(1)

    hacer_Linea(pdf)

    pdf.set_font('Arial', style="B", size=10)
    pdf.cell(0,10, F'Subtotal:$ {importe_subtotal}', ln=True, align='R')
    pdf.cell(0,10, F'Importe Otros Tributos:$ {importe_otros_tributos}', ln=True, align='R')
    pdf.cell(0,10, F'Total:$ {importe_total}', ln=True, align='R')
    
    hacer_Linea(pdf)

    pdf.ln(1)

    pdf.set_font('Arial', style="B", size=10)
    pdf.cell(0,10, F'CAE N.: {n_cae}', ln=True, align='R')
    pdf.cell(0,10, F'Fecha de Vto. de CAE: {fecha_vto_cae}', ln=True, align='R')

    pdf.add_page()

    pdf.rect(5, 5, 200, 287)

    logo_path = 'logo.png'

    pdf.image(logo_path, x=(pdf.w - 20) / 2 - 21, y=21, w=20, h=20)

    pdf.set_font('Arial', style="B", size=20)

    pdf.set_xy(10,10)
    
    hacer_Linea(pdf)
    pdf.cell(0,10, 'DUPLICADO', ln=True, align='C')
    hacer_Linea(pdf)

    x_start = 94.5
    y_start = pdf.get_y()
    line_height = 10 
    num_lines = 7
    y_end = y_start + (line_height * num_lines)
    pdf.set_draw_color(0, 0, 0)
    pdf.line(x_start, y_start, x_start, y_end)


    pdf.set_font('Arial', style="B", size=20)
    pdf.cell(0,10, nombre_fantasia_facturante, align='L')
    pdf.cell(0,10, 'FACTURA', ln=True, align='R')

    pdf.set_font('Arial', style="B", size=10)
    pdf.cell(0,10, F'Razón Social: {razon_social_facturante}', align='L')
    pdf.cell(0,10, F'Punto de Venta: {punto_venta}', ln=True, align='R')
    pdf.cell(0,10, F'Domicilio Comercial: {domicilio_comercial_facturante}', align='L')
    pdf.cell(0,10, F'Comp. Nro: {numero_compra}', ln=True, align='R')
    pdf.cell(0,10, F'Condición Frente al IVA: {condicion_iva_facturante}', align='L')
    pdf.cell(0,10, F'Fecha de Emisión: {fecha_emision_factura}', ln=True, align='R')
    pdf.cell(0,10, F'Cuit: {cuit_facturante}', ln=True, align='R')
    pdf.cell(0,10, F'Ingresos Brutos: {ingresos_brutos_facturante}', ln=True, align='R')
    pdf.cell(0,10, F'Fecha de Inicio de Actividades: {fecha_inicio_actividad_facturante}', ln=True, align='R')

    pdf.set_font('Arial', style="B", size=10)

    texto_completo = F'{tipo_factura}\nCódigo: {codigo_tipo_factura}'

    ancho_texto = pdf.get_string_width(texto_completo)
    ancho_celda = ancho_texto + 6

    x_centrada = (pdf.w - 20) / 2
    y_inicial = 20

    pdf.set_xy(x_centrada, y_inicial)

    pdf.multi_cell(ancho_celda, 10, texto_completo, border=1, align='C')

    pdf.set_draw_color(0, 0, 0)
    pdf.line(x_centrada, y_inicial, x_centrada + ancho_celda, y_inicial)
    pdf.line(x_centrada, y_inicial + 20, x_centrada + ancho_celda, y_inicial + 20)
    pdf.line(x_centrada, y_inicial, x_centrada, y_inicial + 20)
    pdf.line(x_centrada + ancho_celda, y_inicial, x_centrada + ancho_celda, y_inicial + 20)

    pdf.set_y(y_inicial + 20)

    pdf.ln(50)
    
    ancho_fecha_emision = pdf.get_string_width(f'Período Facturado Desde: {fecha_emision_factura}')
    ancho_fecha_hasta = pdf.get_string_width(f'Hasta: {fecha_limite_factura}') + 50
    ancho_fecha_limite = pdf.get_string_width(f'Fecha de Vto. para el pago: {fecha_limite_factura}')

    hacer_Linea(pdf)
    pdf.set_font('Arial', style="B", size=10)
    pdf.cell(ancho_fecha_emision,10, F'Período Facturado Desde: {fecha_emision_factura}', align='C')
    pdf.cell(ancho_fecha_hasta,10, F'Hasta: {fecha_limite_factura}', align='C')
    pdf.cell(ancho_fecha_limite,10, F'Fecha de Vto. para el pago: {fecha_limite_factura}', ln=True, align='C')
    hacer_Linea(pdf)

    pdf.ln(1)

    hacer_Linea(pdf)
    pdf.cell(0,10, F'Apellido y Nombre / Razón Social: {nombre_apellido_cliente}', ln=True, align='L')
    pdf.cell(0,10, F'Condicion frente al IVA: {condicion_iva_cliente}', ln=True, align='L')
    pdf.cell(0,10, F'Condicion de Venta: {condicion_venta_cliente}', ln=True, align='L')
    hacer_Linea(pdf)

    pdf.ln(1)

    espacio=10

    ancho_codigo = pdf.get_string_width('Código:') + espacio
    ancho_prod_ser = pdf.get_string_width('Producto/Servicio:') + espacio
    ancho_cant = pdf.get_string_width('Código:') + espacio
    ancho_precio_unitario=pdf.get_string_width('Precio Unitario:') + espacio
    ancho_bonif_por=pdf.get_string_width('% Bonif:') + espacio
    ancho_bonif_imp=pdf.get_string_width('Imp. Bonif:') + espacio
    ancho_subtotal=pdf.get_string_width('Subtotal:') + espacio

    hacer_Linea(pdf)
    pdf.cell(ancho_codigo,10, 'Código:', align='L')
    pdf.cell(ancho_prod_ser,10, 'Producto/Servicio:', align='L')
    pdf.cell(ancho_cant,10, 'Cantidad:', align='L')
    pdf.cell(ancho_precio_unitario,10, 'Precio Unitario:', align='L')
    pdf.cell(ancho_bonif_por,10, '% Bonif:', align='L')
    pdf.cell(ancho_bonif_imp,10, 'Imp. Bonif:', align='L')
    pdf.cell(ancho_subtotal,10, 'Subtotal:', ln=True, align='L')
    hacer_Linea(pdf)

    pdf.ln(1)

    hacer_Linea(pdf)
    pdf.set_font('Arial', size=10)
    pdf.cell(ancho_codigo,10, str(codigo_prod_ser), align='L')
    pdf.cell(ancho_prod_ser,10, str(prod_ser), align='L')
    pdf.cell(ancho_cant,10, str(cantidad_prod_ser), align='L')
    pdf.cell(ancho_precio_unitario,10, str(precio_unidad), align='L')
    pdf.cell(ancho_bonif_por,10, str(por_bonificado), align='L')
    pdf.cell(ancho_bonif_imp,10, str(imp_bonificado), align='L')
    pdf.cell(ancho_subtotal,10, str(importe_subtotal), ln=True, align='L')
    hacer_Linea(pdf)

    pdf.ln(1)

    hacer_Linea(pdf)

    pdf.set_font('Arial', style="B", size=10)
    pdf.cell(0,10, F'Subtotal:$ {importe_subtotal}', ln=True, align='R')
    pdf.cell(0,10, F'Importe Otros Tributos:$ {importe_otros_tributos}', ln=True, align='R')
    pdf.cell(0,10, F'Total:$ {importe_total}', ln=True, align='R')

    hacer_Linea(pdf)

    pdf.ln(1)

    pdf.set_font('Arial', style="B", size=10)
    pdf.cell(0,10, F'CAE N.: {n_cae}', ln=True, align='R')
    pdf.cell(0,10, F'Fecha de Vto. de CAE: {fecha_vto_cae}', ln=True, align='R')
    
    pdf_file= f'Factura_{nombre_apellido_cliente}.pdf'
    pdf.output(pdf_file, 'F')
    messagebox.showinfo('Factura Generada')

root = tk.Tk()
root.title('Generador de Facturas')

frame = ttk.Frame(root, padding = '10')
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

generar_factura_btn=ttk.Button(frame, text='Generar Factura', command=generar_factura)
generar_factura_btn.grid(row=7, column=0, columnspan=2)

root.mainloop()