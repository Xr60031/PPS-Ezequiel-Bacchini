from interfaz_wsfev1 import InterfazWSFEv1
from Facades.Excel.facade_dataframes import Facade_dataframe
from impresor_pdf.impresor_pdf import Impresor_PDF
from Facades.Facturacion.facade_historial import Facade_Historial

from Funciones.Ensambladores.armar_historial import Armador_Historial
from Funciones.ZIP.zip_manager import Zip_Manager
import zipfile

from Constantes.Facturacion.constantes_arrays import constantes_historial, constantes_CAE, constantes_PDF

import io
import os


class Facade_facturacion():
    def __init__(self):
        self
    
    def __facturar(self, wsfve, llave, certificado, cuit, datos_factura, biblioteca_datos_vendedor, tipo_factura):
        print("Conectando a los servicios web de AFIP/ARCA. . .")
        wsfve.conectar(llave, certificado, cuit)
        print("Facturando. . .")
        return wsfve.facturar(datos_factura, biblioteca_datos_vendedor, tipo_factura)
        
    def facturacion(self, file_name, llave, certificado, biblioteca_datos_vendedor, datos_factura, dataframe_historial):
        factura = 0

        wsfve = InterfazWSFEv1()
        zip_buffer = io.BytesIO()
        facade_historial = Facade_Historial()
        impresor_pdf = Impresor_PDF()
        zip_writer = Zip_Manager()
        ensamblador_historial = Armador_Historial()

        ID = datos_factura[factura]["Identificador_Factura"]
        ID_anterior = None

        with zipfile.ZipFile(zip_buffer,  "w", zipfile.ZIP_DEFLATED) as zipf:
            while factura < len(datos_factura) and ID != None:
                ID = datos_factura[factura]["Identificador_Factura"]
                if(ID_anterior == None or ID != ID_anterior):
                    #facturo
                    datos_CAE = self.__facturar(wsfve, llave, certificado, str(biblioteca_datos_vendedor["CUIT"]), datos_factura[factura], biblioteca_datos_vendedor, datos_factura[factura]["ID_factura_nota"])

                    #Imprime la factura
                    pdf_contenido = impresor_pdf.generar_pdf_(
                        datos_factura[factura],
                        biblioteca_datos_vendedor,
                        datos_CAE
                    )

                    zipf = zip_writer.zip_write_str(zipf, f"factura_{datos_CAE[constantes_CAE.CAE.value]}{factura}.pdf", pdf_contenido[constantes_PDF.pos_contenido_pdf.value])

                    datos_historial = []
                    ensamblador_historial.build_datos_historial(datos_historial, datos_factura[factura], datos_factura[factura]["items"], datos_factura[factura]["tributos"], biblioteca_datos_vendedor, datos_CAE)

                    row_next_historial = facade_historial.obtener_row_historial(dataframe_historial[constantes_historial.excel_hoja_historial.value])
                    facade_historial.escribir_historial(datos_historial, dataframe_historial[constantes_historial.excel_hoja_historial.value], row_next_historial)

                    facade_historial.guardar_historial(dataframe_historial[constantes_historial.excel_dataframe.value], file_name)
            
                ID_anterior = ID
                factura += 1

            dataframe_manager = Facade_dataframe()
            xml = f'uploads/Ticket_Acceso{biblioteca_datos_vendedor["CUIT"]}.xml'
            with open(xml, 'r', encoding='utf-8') as f:
                content = f.read()
            dataframe_manager.guardar_xml(file_name, content)
            zipf = zip_writer.zip_write(zipf, file_name, os.path.basename(file_name))
        
        return zip_buffer