from abc import ABC, abstractmethod
from fpdf import FPDF
import os
import segno
from io import BytesIO
from impresor_pdf.templates.enums import X_pos
from Constantes.Facturacion.constantes_arrays import constantes_CAE
class Template(ABC):
    def __init__(self, tipo_factura_nota, codigo_tipo_factura_nota, factura_nota):
        super().__init__()
        self.no_aplica = "No Aplica"
        self.pdf = None
        self.identacion_grande = 15
        self.identacion_chica = 5
        self.tipo_factura_nota = tipo_factura_nota
        self.codigo_tipo_factura_nota = codigo_tipo_factura_nota
        self.tamaño_letra_titulo = 18
        self.tamaño_letra_subtitulo = 10
        self.tamaño_letra_parrafo = 8
        self.fuente = 'Arial'
        self.tipo= factura_nota

    def hacer_identificador_nota(self, punto_venta, numero_comprobante):
        cant_car_pventa = len(str(punto_venta))
        cant_car_n_comprobante = len(str(numero_comprobante))

        id = "0" * (4 - cant_car_pventa) + f"{punto_venta}" + "-" + "0" * (9 - cant_car_n_comprobante) + f"{numero_comprobante}"
        return id

    def hacer_salto_de_linea(self, cant_saltos):
        self.pdf.ln(cant_saltos)

    def establecer_posicion(self, X, Y):
        self.pdf.set_xy(X,Y)
    
    def establecer_tamaño_fuente(self, tamaño):
        self.pdf.set_font(self.fuente, style="B", size=tamaño)
        
    def añadir_pagina(self):
        self.pdf.add_page()

    def generar_marco_externo(self):
        self.pdf.rect(5, 5, 200, 287)

    def hacer_Linea(self):
        self.pdf.line(self.pdf.get_x(), self.pdf.get_y(), self.pdf.w-10, self.pdf.get_y())

    def armar_pdf_nuevo(self):
        self.pdf = FPDF()

    def requiere_pagina_duplicado(self, iteracion):
        if(iteracion == 1):
            self.añadir_pagina()

    def armar_encabezado(self, iteracion):
        self.establecer_tamaño_fuente(self.tamaño_letra_titulo)
        self.establecer_posicion(10,10)
        self.hacer_Linea()
        if(iteracion == 1):
            self.pdf.cell(0,10, 'ORIGINAL', ln=True, align='C')
        else:
            self.pdf.cell(0,10, 'DUPLICADO', ln=True, align='C')
        self.hacer_Linea()

        x_start = 94.5
        y_start = self.pdf.get_y()
        line_height = 10 
        num_lines = 7
        y_end = y_start + (line_height * num_lines)
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.line(x_start, y_start, x_start, y_end)

    def armar_titulo(self, biblioteca_datos_vendedor):
        self.establecer_tamaño_fuente(self.tamaño_letra_titulo)

        self.pdf.cell(0,self.identacion_grande, biblioteca_datos_vendedor["Nombre_Empresa"], align='L')
        self.pdf.cell(0,self.identacion_grande, self.tipo, ln=True, align='R')

    def armar_datos_usuario_comunes(self, biblioteca_datos_vendedor, datos_CAE, datos_factura):
        datos_usuario_comunes = [
            F'Razón Social: {biblioteca_datos_vendedor["Razon_Social"]}',
            F'Punto de Venta: {biblioteca_datos_vendedor["Punto_de_venta"]}',
            F'Domicilio Comercial: {biblioteca_datos_vendedor["Domicilio"]}',
            F'Comp. Nro: {int(datos_CAE[2])}',
            F'Condición Frente al IVA: {biblioteca_datos_vendedor["Condicion_frente_al_IVA"]}',
            F'Fecha de Emisión: {datos_factura["fecha_emision"]}',
            F'Cuit: {biblioteca_datos_vendedor["CUIT"]}',
            F'Ingresos Brutos: {biblioteca_datos_vendedor["Ingresos_Brutos"]}',
            F'Fecha de Inicio de Actividades: {biblioteca_datos_vendedor["Fecha_Inicio"]}'
        ]

        return datos_usuario_comunes
    
    @abstractmethod
    def armar_datos_usuario_opcionales(self, biblioteca_datos_vendedor, datos_CAE, datos_factura):
        pass
    
    @abstractmethod
    def unir_datos_usuario(self, datos_comunes, datos_opcionales):
        pass
    
    def armar_datos_usuario_unificado(self, datos_unificados):
        self.establecer_tamaño_fuente(self.tamaño_letra_parrafo)
        for i in range(len(datos_unificados)):
            if(i%2 != 0):
                self.pdf.cell(0,self.identacion_chica+2, datos_unificados[i], align='L')
            else: self.pdf.cell(0,self.identacion_chica+2, datos_unificados[i], ln=True, align='R')

    def armar_codigo_factura(self):
        self.establecer_tamaño_fuente(self.tamaño_letra_subtitulo)

        texto_completo = F'{self.tipo_factura_nota}\nCódigo: {self.codigo_tipo_factura_nota}'

        ancho_texto = self.pdf.get_string_width(texto_completo)
        ancho_celda = ancho_texto + 6

        x_centrada = (self.pdf.w - 20) / 2
        y_inicial = 20

        self.establecer_posicion(x_centrada, y_inicial)

        self.pdf.multi_cell(ancho_celda, self.identacion_chica, texto_completo, border=1, align='C')

        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.line(x_centrada, y_inicial, x_centrada + ancho_celda, y_inicial)
        self.pdf.line(x_centrada, y_inicial + 10, x_centrada + ancho_celda, y_inicial + 10)
        self.pdf.line(x_centrada, y_inicial, x_centrada, y_inicial + 10)
        self.pdf.line(x_centrada + ancho_celda, y_inicial, x_centrada + ancho_celda, y_inicial + 10)

        self.pdf.set_y(y_inicial + 20)

        self.hacer_salto_de_linea(50)

    def armar_fechas(self, datos_factura):
        self.establecer_tamaño_fuente(self.tamaño_letra_parrafo)

        ancho_fecha_desde = self.pdf.get_string_width(f'Período Facturado Desde: {datos_factura["Fecha_servicio_desde"] or self.no_aplica}')
        ancho_fecha_hasta = self.pdf.get_string_width(f'Hasta: {datos_factura["Fecha_servicio_hasta"] or self.no_aplica}') + 50
        ancho_fecha_limite = self.pdf.get_string_width(f'Fecha de Vto. para el pago: {datos_factura["Fecha_vencimiento_de_pago"] or self.no_aplica}')

        self.hacer_Linea()

        self.establecer_tamaño_fuente(self.tamaño_letra_parrafo)
        self.pdf.cell(ancho_fecha_desde,10, F'Período Facturado Desde: {datos_factura["Fecha_servicio_desde"] or self.no_aplica}', align='C')
        self.pdf.set_x(self.pdf.get_x() - 13)
        self.pdf.cell(ancho_fecha_hasta,10, F'Hasta: {datos_factura["Fecha_servicio_hasta"] or self.no_aplica}', align='C')
        self.pdf.set_x(self.pdf.get_x() - 15)
        self.pdf.cell(ancho_fecha_limite,10, F'Fecha de Vto. para el pago: {datos_factura["Fecha_vencimiento_de_pago"] or self.no_aplica}', ln=True, align='C')
        
        self.hacer_Linea()

        self.hacer_salto_de_linea(1)

    def armar_datos_cliente_comunes(self, datos_factura):
        datos_comunes = [
            F'Apellido y Nombre / Razón Social: {datos_factura["Nombre_y_Apellido_Cliente"]}',
            F'Condicion frente al IVA: {datos_factura["Condicion_frente_al_IVA_Cliente"]}',
            F'Condicion de Venta: {datos_factura["Condicion_de_venta_Cliente"]}'
        ]

        return datos_comunes

    @abstractmethod
    def armar_datos_cliente_opcionales(self, datos_factura):
        pass

    @abstractmethod
    def unir_datos_cliente(self, datos_comunes, datos_opcionales):
        pass

    def armar_datos_cliente_unificado(self, datos_cliente):

        for i in range(len(datos_cliente)):
            if(i%2 != 0):
                self.pdf.cell(0,self.identacion_chica, datos_cliente[i], ln=True, align='R')
            else: self.pdf.cell(0,self.identacion_chica, datos_cliente[i], align='L')

        self.hacer_salto_de_linea(5)
        self.hacer_Linea()
        

    def armar_titulos_items_comunes(self):
        datos_comunes = [
            #Posicion X
            #Alineacion
            #Contenido
            [
                X_pos.CODIGO.value, 
                20,
                'Código:' 
            ],
            [
                X_pos.ITEM.value, #A partir del segundo se le suma el valor de X anterior
                60,
                'Producto/Servicio:'
            ],
            [
                X_pos.CANTIDAD.value,
                20,
                'Cantidad:'
            ],
            [
                X_pos.PRECIO_UNITARIO.value,
                10,
                'Precio Unitario:'
            ],
            [
                X_pos.POR_BONIFICADO.value,
                10,
                '% Bonif:'
            ],
            [
                X_pos.IMP_BONIFICADO.value,
                10,
                'Imp. Bonif:'
            ],
            [
                X_pos.SUBTOTAL.value,
                40,
                'Subtotal:'
            ]
        ]

        return datos_comunes

    @abstractmethod
    def armar_titulos_items_opcionales(self):
        pass

    @abstractmethod
    def unir_titulos_items(self, titulos_comunes, titulos_opcional):
        pass

    def armar_titulos_items_unificado(self, titulos_items):
        self.establecer_tamaño_fuente(self.tamaño_letra_parrafo)

        X_anterior = 0
        for i in range(len(titulos_items)):
            self.pdf.set_x(titulos_items[i][0] + X_anterior)
            self.pdf.cell(titulos_items[i][1],self.identacion_chica, titulos_items[i][2], align='L')
            X_anterior = titulos_items[i][0] + X_anterior

        self.hacer_salto_de_linea(5)
        self.hacer_Linea()

    def armar_items_comunes(self, datos_factura):
        datos_comunes = []
        for cant in range(len(datos_factura["items"])):
            item_actual = []
            item_actual.extend([
                #Posicion X
                #Alineacion
                #Contenido
                [
                    X_pos.CODIGO.value, 
                    40,
                    str(datos_factura["items"][cant][3]) 
                ],
                [
                    X_pos.ITEM.value, #A partir del segundo se le suma el valor de X anterior
                    20,
                    str(datos_factura["items"][cant][0])
                ],
                [
                    X_pos.CANTIDAD.value,
                    20,
                    str(int(datos_factura["items"][cant][2]))
                ],
                [
                    X_pos.PRECIO_UNITARIO.value,
                    20,
                    str(datos_factura["items"][cant][5])
                ],
                [
                    X_pos.POR_BONIFICADO.value,
                    30,
                    str(datos_factura["items"][cant][1])
                ],
                [
                    X_pos.IMP_BONIFICADO.value,
                    20,
                    str(datos_factura["items"][cant][7])
                ],
                [
                    X_pos.SUBTOTAL.value,
                    20,
                    str(datos_factura["items"][cant][8])
                ]
            ])

            datos_comunes.append(item_actual)
        return datos_comunes
    
    @abstractmethod
    def armar_items_opcionales(self, datos_factura):
        pass
    
    @abstractmethod
    def unir_items(self, items_comunes, items_opcionales):
        pass

    def armar_items_unificado(self, items, cant_titulos):
        for i in items:
            if self.pdf.get_y() > self.pdf.h - self.pdf.b_margin:
                self.añadir_pagina()
                self.establecer_tamaño_fuente(8)
        
        self.establecer_tamaño_fuente(8)
        self.hacer_salto_de_linea(2)
        for i in range(len(items)):
            j = 0
            X_anterior = 0
            while j < cant_titulos:
                self.pdf.set_x(items[i][j][0] + X_anterior)
                self.pdf.cell(items[i][j][1],5, items[i][j][2], align='L')
                X_anterior = items[i][j][0] + X_anterior
                j+=1
            self.hacer_salto_de_linea(4)
            
        

        self.hacer_Linea()

    def armar_subtotales_comunes(self, datos_factura):
        datos_comunes = [
            F'Subtotal:$ {int((datos_factura["Importe_Total"]-datos_factura["Importe_Tributo"])*100)/100}',
            F'Importe Otros Tributos:$ {datos_factura["Importe_Tributo"]}',
            F'Total:$ {datos_factura["Importe_Total"]}'
        ]

        return datos_comunes
    
    @abstractmethod
    def armar_subtotales_opcionales(self, datos_factura):
        pass

    @abstractmethod
    def unir_subtotales(self, subtotales_comunes, subtotales_opcionales):
        pass

    def armar_subtotales_unificado(self, datos_subtotales):
        self.establecer_tamaño_fuente(10)
        for i in range(len(datos_subtotales)):
            self.pdf.cell(0,self.identacion_chica, datos_subtotales[i], ln=True, align='R')
        self.hacer_Linea()
        self.hacer_salto_de_linea(1)

    def armar_datos_cae(self, datos_CAE):
        self.establecer_tamaño_fuente(10)
        self.pdf.cell(0, self.identacion_chica, F'CAE N.: {datos_CAE[0]}', ln=True, align='R')
        self.pdf.cell(0, self.identacion_chica, F'Fecha de Vto. de CAE: {datos_CAE[1]}', ln=True, align='R')

    def armar_qr(self, qr_content, qr_filename):
        qr_buffer = segno.make(qr_content)
        qr_buffer_io = BytesIO()
        qr_buffer.save(qr_buffer_io, kind="png", scale=5)
        qr_buffer_io.seek(0)

        with open(qr_filename,"wb") as f:
            f.write(qr_buffer_io.getvalue())

        qr_x = 10
        qr_y = 265
        qr_size = 25

        self.pdf.image(qr_filename, x=qr_x, y=qr_y, w=qr_size, h=qr_size)
        self.pdf.set_auto_page_break(auto=True, margin=5)

        image_x = qr_x  + qr_size + 6
        image_y = qr_y 
        image_w = 50  # Ancho de la imagen
        image_h = 15  # Alto de la imagen

        self.pdf.image('impresor_pdf/Arca_logo.jpg', x=image_x, y=image_y, w=image_w, h=image_h)

        text_x = qr_x + qr_size + 5
        text_y = qr_y
        self.establecer_posicion(text_x, text_y+15)
        self.establecer_tamaño_fuente(8)
        self.pdf.cell(0, self.identacion_chica, 'Comprobante Autorizado', ln=True, align='L')

        self.establecer_posicion(text_x, text_y+20)
        self.establecer_tamaño_fuente(6)
        self.pdf.cell(0, self.identacion_chica, 'Esta Administración Federal no se responsabiliza por los datos ingresados en el detalle de la operación', ln=True, align='L')

    def generar_pdf(self,
        datos_factura,
		biblioteca_datos_vendedor,
		datos_CAE,
        qr_content,
        qr_filename
    ):
        iteracion = 1
        self.armar_pdf_nuevo()
        self.añadir_pagina()
        while iteracion < 3:
            self.generar_marco_externo()

            self.armar_encabezado(iteracion)

            self.armar_titulo(biblioteca_datos_vendedor)

            self.armar_datos_usuario_unificado(
                self.unir_datos_usuario(
                    self.armar_datos_usuario_comunes(biblioteca_datos_vendedor, datos_CAE, datos_factura), 
                    self.armar_datos_usuario_opcionales(biblioteca_datos_vendedor, datos_CAE, datos_factura)
                )
            )
            
            self.armar_codigo_factura()

            self.armar_fechas(datos_factura)

            self.armar_datos_cliente_unificado(
                self.unir_datos_cliente(
                    self.armar_datos_cliente_comunes(datos_factura),
                    self.armar_datos_cliente_opcionales(datos_factura)
                )    
            )

            titulos_unificados = self.unir_titulos_items(
                                    self.armar_titulos_items_comunes(),
                                    self.armar_titulos_items_opcionales()
                                )
            
            self.armar_titulos_items_unificado(
                titulos_unificados
            )

            self.armar_items_unificado(
                self.unir_items(
                    self.armar_items_comunes(datos_factura),
                    self.armar_items_opcionales(datos_factura)
                ),
                len(titulos_unificados)
            )

            self.armar_subtotales_unificado(
                self.unir_subtotales(
                    self.armar_subtotales_comunes(datos_factura),
                    self.armar_subtotales_opcionales(datos_factura)
                )
            )

            self.armar_datos_cae(datos_CAE)

            self.armar_qr(qr_content, qr_filename)

            self.requiere_pagina_duplicado(iteracion)

            iteracion += 1
        os.remove(qr_filename)
        answer = []
        answer.append(datos_CAE[constantes_CAE.ultimo_comprobante_autorizado.value])
        answer.append(self.pdf.output(dest='S').encode('latin1'))
        return answer
