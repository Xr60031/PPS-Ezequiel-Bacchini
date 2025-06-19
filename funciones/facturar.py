from interfaz_wsfev1 import InterfazWSFEv1
from Facades.facade_dataframes import Facade_dataframe

from impresor_pdf.impresor_pdf import generar_pdf_
from ExcelManager.historial_manager import escribir_historial, obtener_row_historial, guardar_historial

from Funciones.Ensambladores.armar_historial import build_datos_historial
from Funciones.zip_manager import zip_write, zip_write_str
import zipfile

import io
import os

def facturar(wsfve, llave, certificado, cuit, datos_factura, biblioteca_datos_vendedor, tipo_factura):
  print("Conectando a los servicios web de AFIP/ARCA. . .")
  wsfve.conectar(llave, certificado, cuit)
  print("Facturando. . .")
  return wsfve.facturar(datos_factura, biblioteca_datos_vendedor, tipo_factura)

#Funcion para realizar el proceso de facturacion
def facturacion(file_name, llave, certificado, biblioteca_datos_vendedor, datos_factura, dataframe_historial):
  factura = 0

  wsfve = InterfazWSFEv1()
  zip_buffer = io.BytesIO()

  ID = datos_factura[factura]["Identificador_Factura"]
  ID_anterior = None

  with zipfile.ZipFile(zip_buffer,  "w", zipfile.ZIP_DEFLATED) as zipf:
    while factura < len(datos_factura) and ID != None:
      ID = datos_factura[factura]["Identificador_Factura"]
      if(ID_anterior == None or ID != ID_anterior):
        #facturo
        datos_CAE = facturar(wsfve, llave, certificado, str(biblioteca_datos_vendedor["CUIT"]), datos_factura[factura], biblioteca_datos_vendedor, datos_factura[factura]["ID_factura_nota"])

        #Imprime la factura
        pdf_contenido = generar_pdf_(
          datos_factura[factura],
          biblioteca_datos_vendedor,
          datos_CAE
        )

        zipf = zip_write_str(zipf, f"factura_{datos_CAE[0]}{factura}.pdf", pdf_contenido[1])

        datos_historial = []
        build_datos_historial(datos_historial, datos_factura[factura], datos_factura[factura]["items"], datos_factura[factura]["tributos"], biblioteca_datos_vendedor, datos_CAE)

        row_next_historial = obtener_row_historial(dataframe_historial[1])
        escribir_historial(datos_historial, dataframe_historial[1], row_next_historial)

        guardar_historial(dataframe_historial[0], file_name)
      
      ID_anterior = ID
      factura += 1

    dataframe_manager = Facade_dataframe()
    xml = f'uploads/Ticket_Acceso{biblioteca_datos_vendedor["CUIT"]}.xml'
    with open(xml, 'r', encoding='utf-8') as f:
        content = f.read()
    dataframe_manager.guardar_xml(file_name, content)
    zipf = zip_write(zipf, file_name, os.path.basename(file_name))
  
  return zip_buffer