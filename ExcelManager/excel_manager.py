from interfaz_wsfev1 import InterfazWSFEv1
from impresor_pdf.impresor_pdf import generar_pdf_
import zipfile
import io
import os
from facades.Persistencia.facade_dataframes import Facade_dataframe
from Constantes import constantes_excel

#Builea el array que contiene todos los datos para que sean escritos en el historial
def build_datos_historial(datos_historial, datos_factura, productos_servicios, tributos, biblioteca_datos_vendedor, datos_cae):
  datos_historial.append(datos_factura["Identificador_Factura"])
  datos_historial.append(datos_factura["tipo_factura_nota"])
  datos_historial.append(datos_factura["Nombre_y_Apellido_Cliente"])
  datos_historial.append(datos_factura["Tipo_Documento"])
  datos_historial.append(datos_factura["Numero_de_documento_del_cliente"])
  datos_historial.append(datos_factura["Condicion_de_venta_Cliente"])
  datos_historial.append(datos_factura["Condicion_frente_al_IVA_Cliente"])
  datos_historial.append(datos_factura["Concepto"])
  datos_historial.append(datos_factura["Fecha_servicio_desde"])
  datos_historial.append(datos_factura["Fecha_servicio_hasta"])
  datos_historial.append(datos_factura["Fecha_vencimiento_de_pago"])
  datos_historial.append(productos_servicios)
  datos_historial.append(datos_factura["Importe_Neto"])
  datos_historial.append(datos_factura["Importe_Total"])
  datos_historial.append(datos_factura["Importe_Tributo"])
  datos_historial.append(tributos)
  datos_historial.append(biblioteca_datos_vendedor["Nombre"])
  datos_historial.append(biblioteca_datos_vendedor["CUIT"])
  datos_historial.append(biblioteca_datos_vendedor["Nombre_Empresa"])
  datos_historial.append(biblioteca_datos_vendedor["Punto_de_venta"])
  datos_historial.append(biblioteca_datos_vendedor["Razon_Social"])
  datos_historial.append(biblioteca_datos_vendedor["Domicilio"])
  datos_historial.append(biblioteca_datos_vendedor["Condicion_frente_al_IVA"])
  datos_historial.append(biblioteca_datos_vendedor["Ingresos_Brutos"])
  datos_historial.append(biblioteca_datos_vendedor["Fecha_Inicio"])
  datos_historial.append(biblioteca_datos_vendedor["iag"])
  datos_historial.append(biblioteca_datos_vendedor["desc_iag"])
  datos_historial.append(biblioteca_datos_vendedor["alicuota"])
  datos_historial.append(datos_cae[0]),
  datos_historial.append(datos_cae[1]),
  datos_historial.append(datos_cae[2])
  return

#Escribe el historial 
def escribir_historial(datos_historial, historial_hoja, row):

  cant_var = 1
  i = 0
  while i < constantes_excel.limite_hasta_items:
    historial_hoja.cell(row=row, column=cant_var, value=datos_historial[i])
    cant_var += 1
    i += 1

  cant_var_ant = cant_var
  row_ant = row
  j = 0
  k = 0
  productos_servicios = datos_historial[constantes_excel.limite_hasta_items]
  while j < len(productos_servicios):
    k = 0
    cant_var = cant_var_ant
    while k < constantes_excel.cant_datos_items:
      historial_hoja.cell(row=row, column=cant_var, value=productos_servicios[j][k])
      k += 1
      cant_var += 1
    row += 1
    j += 1

  i += 1
  row = row_ant

  while i < constantes_excel.limite_hasta_tributos:
    historial_hoja.cell(row=row, column=cant_var, value=datos_historial[i])
    cant_var += 1
    i += 1

  cant_var_ant = cant_var
  row_ant = row
  j = 0
  k = 1
  tributos = datos_historial[constantes_excel.limite_hasta_tributos]
  if len(tributos) > 0:
    while j < len(tributos):
      k = 0
      cant_var = cant_var_ant
      while k < constantes_excel.cant_datos_tributos:
        historial_hoja.cell(row=row, column=cant_var, value=tributos[j][k])
        k += 1
        cant_var += 1
      row += 1
      j += 1
  else:
    cant_var += constantes_excel.cant_filas_a_saltear
  i += 1
  row = row_ant

  while i < constantes_excel.numero_finalizacion:
    historial_hoja.cell(row=row, column=cant_var, value=datos_historial[i])
    cant_var += 1
    i += 1

def zip_write_str(zipf, name, content):
  zipf.writestr(name, content)
  return zipf

def zip_write(zipf, name, content):
  zipf.write(name, content)
  return zipf

def obtener_row_historial(dataframe_historial):
  row = 2
  while dataframe_historial.cell(row=row, column=1).value:
    row += 1
  
  return row

def guardar_historial(dataframe_historial, file_name):
  dataframe_historial.save(file_name)

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




