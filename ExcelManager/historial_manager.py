from openpyxl import load_workbook

def obtener_historial(path_excel):
    excel_dataframe=load_workbook(path_excel, data_only=True)
    historial= excel_dataframe["Historial"]
    datos_totales = []
    datos_actual = []
    row = 2
    while historial.cell(row=row, column=1).value:
      columna = 1
      while(columna < 45):
        datos_actual.append(historial.cell(row=row, column=columna).value)
        columna += 1
      datos_totales.append(datos_actual)
      datos_actual = []
      row += 1

    return datos_totales