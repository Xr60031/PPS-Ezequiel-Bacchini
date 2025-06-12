from Funciones.obtenerdor_IDs import obtener_ID_tributo

#Arma la biblioteca con los datos del vendedor
def armar_biblioteca_vendedor(datos_vendedor):
    bibloteca_datos_vendedor = {
        "Nombre": datos_vendedor[0],
        "CUIT": datos_vendedor[1],
        "Nombre_Empresa": datos_vendedor[2],
        "Punto_de_venta": datos_vendedor[3],
        "Razon_Social": datos_vendedor[4],
        "Domicilio": datos_vendedor[5],
        "Condicion_frente_al_IVA": datos_vendedor[6],
        "Ingresos_Brutos": datos_vendedor[7],
        "Fecha_Inicio": datos_vendedor[8],
        "iag": datos_vendedor[9],
        "desc_iag": datos_vendedor[10],
        "alicuota": datos_vendedor[11],
        "id_tributo_global": obtener_ID_tributo(datos_vendedor[9])
    }

    return bibloteca_datos_vendedor