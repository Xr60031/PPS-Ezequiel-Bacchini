def obtener_digitos_cuit(CUIT): 
    primeros_diez_digitos = []
    for i in range(10):
        primeros_diez_digitos.append(CUIT[i])
    return primeros_diez_digitos

def calcular_peso(primeros_diez_digitos):
    return int(primeros_diez_digitos[0])*5 + int(primeros_diez_digitos[1])*4 + int(primeros_diez_digitos[2])*3 + int(primeros_diez_digitos[3])*2 + int(primeros_diez_digitos[4])*7 + int(primeros_diez_digitos[5])*6 + int(primeros_diez_digitos[6])*5 + int(primeros_diez_digitos[7])*4 + int(primeros_diez_digitos[8])*3 + int(primeros_diez_digitos[9])*2

def verificar_cuit(CUIT):
    str_CUIT = str(CUIT)
    if len(str_CUIT) == 11:
        #PDD -> primeros dos digitos
        PDD = str_CUIT[:2]
        if PDD in ['20', '23', '24', '27', '30', '33', '34']:
            CUIT_raw = obtener_digitos_cuit(str_CUIT[:10])
            Peso_CUIT = calcular_peso(CUIT_raw)
            Resultado = Peso_CUIT % 11
            if Resultado == 1:
                return False
            elif Resultado != 0:
                Resultado = 11 - Resultado
                    

            
            if int(str_CUIT[10]) == Resultado:
                return True
    return False

