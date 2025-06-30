import importlib
import datetime
from interfaz_wsaa import InterfazWSAA
from Exceptions.Exceptions_Custom.exception_error_factura import ErrorFacturacion

wsfev1_lib = importlib.import_module("PYAFIPWS.pyafipws-main.wsfev1")

wsfev1 = wsfev1_lib.WSFEv1()
wsfev1.LanzarExcepciones = True

class InterfazWSFEv1():
    _public_methods_ = [
        "inicializar", # conecta el servicio WSFEv1 y crea un ticket de acceso a traves de WSAA
        "facturar_prueba",
            # tipos:
            #   proyectos   - proyectos promovidos
            #   usados      - RG Bienes Usados 3411 (del vendedor)
            #   rg3668      - RG 3668 Impuesto al Valor Agregado - Art.12
            #   rg4004      - RG 4004-E Alquiler de inmuebles (Ganancias)
            #   rg4109      - RG 4109-E bienes muebles registrables (%)
            #   fce         - Factura de Crédito Electrónica MiPyMEs (FCE)
            #   rg4540      - ?
            #   rg5259      - ?
            #
            # opciones:
            #   multiple    - permite autorizar multiples comprobantes simultaneos
            #   caea        - sistema de respaldo cuando el sistema de AFIP esta caido
            #   reprocesar  - solicita el CAE de nuevo y verifica que sea igual (creo)
            #   consultar   - revisa que los datos del comprobante solicitado sean los mismos que los pedidos

        #"get", # muestra datos del ultimo comprobante autorizado
        #"parametros", # muestra los posibles valores que podes establecer en cada campo del comprobante (creo)
        #"cotizacion", # muestra la cotizacion del dólar
        #"comptox", # muestra cantidad maxima de comprobantes posibles por pedido
        #"ptosventa", # muestra los puntos de venta registrados
        #"solicitarCAEA", # solicita (o consulta) un CAEA
        #"sinMovimientoCAEA" # informa CAEA sin movimiento
        "facturar",
        "conectar",
        "hacer_nota_credito"

    ]

    _public_attrs_ = [
        
    ]

    #Reemplazar cuit, clave y key por las propias para poder utilizar la función de prueba
    def inicializar(self):
        ok = wsfev1.Conectar(
            None,
            "https://wswhomo.afip.gov.ar/wsfev1/service.asmx?WSDL", # es el URL de homologación
            None,
            None,
            r"CERTIFICADOS\cacert.pem"
        )

        if not ok:
            raise RuntimeError(wsfev1.Excepcion)
        
        # obteniendo el TA para pruebas
        ta = InterfazWSAA().Crear_Ticket_Acceso_Firmado(
            service="wsfe",
            certificado="path a archivo de certificado.crt",
            clave="path a archivo de clave_privada.key",
            cuit="cuit vendedor"
        )
        wsfev1.SetTicketAcceso(ta)
        wsfev1.Cuit = "cuit vendedor"
    

    def facturar_prueba(self):
        #print(wsfev1.client.help("FECAESolicitar").encode("latin1"))

        tipo_cbte = 1
        concepto = 1
        punto_vta = 12
        cbte_nro = int(wsfev1.CompUltimoAutorizado(tipo_cbte, punto_vta) or 0)
        fecha = datetime.datetime.now().strftime("%Y%m%d")
        tipo_doc = 80
        nro_doc = "20111111112"
        cbt_desde = cbte_nro + 1
        cbt_hasta = cbte_nro + 1
        imp_total = "184.05"
        imp_tot_conc = "0.00"
        imp_neto = "150.00"
        imp_iva = "26.25"
        imp_trib = "7.80"
        imp_op_ex = "0.00"
        fecha_cbte = fecha
        #fecha_venc_pago = fecha_serv_desde = fecha_serv_hasta = None
        #Fechas del período del servicio facturado y vencimiento de pago:
        
        #fecha_venc_pago = fecha
        #fecha_serv_desde = fecha
        #fecha_serv_hasta = fecha

        moneda_id = "PES"
        moneda_ctz = "1.000" ### ESTABLECE TODOS LOS DATOS
        cancela_misma_moneda_ext='N'
        condicion_iva_receptor_id=5

        reg_x_req = 1  # un solo comprobante

        for i in range(reg_x_req):

            resultado = wsfev1.CrearFactura(### CREA LA FACTURA CON LOS DATOS
                concepto,
                tipo_doc,
                nro_doc,
                tipo_cbte,
                punto_vta,
                cbt_desde + i,
                cbt_hasta + i,
                imp_total,
                imp_tot_conc,
                imp_neto,
                imp_iva,
                imp_trib,
                imp_op_ex,
                fecha_cbte,
                None,
                None,
                None,  # --
                moneda_id,
                moneda_ctz,
                condicion_iva_receptor_id,
                cancela_misma_moneda_ext,
            )

            # comprobantes asociados (notas de crédito / débito)
            if tipo_cbte in (2, 3, 7, 8, 12, 13, 202, 203, 208, 213):       ### ESTABLECE COMPROBANTES ASOCIADOS
                tipo = 201 if tipo_cbte in (202, 203, 208, 213) else 3
                pto_vta = punto_vta
                nro = 1
                cuit = "20462668318"
                # obligatorio en Factura de Crédito Electrónica MiPyMEs (FCE):
                fecha_cbte = fecha if tipo_cbte in (3, 202, 203, 208, 213) else None
                wsfev1.AgregarCmpAsoc(tipo, pto_vta, nro, cuit, fecha_cbte)

            # otros tributos:
            tributo_id = 99                                                 ### ESTABLECE TRIBUTOS (IMPUESTOS)
            desc = "Impuesto Municipal Matanza"
            base_imp = 150
            alic = 5.2
            importe = 7.8
            wsfev1.AgregarTributo(tributo_id, desc, base_imp, alic, importe)

            # subtotales por alicuota de IVA:                               ### ESTABLECE IVA (21%)
            iva_id = 5  # 21%
            base_imp = 100
            importe = 21
            wsfev1.AgregarIva(iva_id, base_imp, importe)

            iva_id = 4  # 5.25%
            base_imp = 50
            importe = 5.25
            wsfev1.AgregarIva(iva_id, base_imp, importe)
        
        cae = wsfev1.CAESolicitar()                                               ### SOLICITA EL CAE

        print(resultado)
        for i in range(reg_x_req):
            print("Nro. Cbte. desde-hasta", wsfev1.CbtDesde, wsfev1.CbtHasta)
            print("Resultado", wsfev1.Resultado)
            print("Reproceso", wsfev1.Reproceso)
            print("CAE", cae)
            print("Vencimiento", wsfev1.Vencimiento)
            print("Observaciones", wsfev1.Obs)

    #URL de produccion "https://servicios1.afip.gov.ar/wsfev1/service.asmx?WSDL"
    def conectar(self, llave_, certificado_, cuit_):
        ok = wsfev1.Conectar(
            None,
            "https://wswhomo.afip.gov.ar/wsfev1/service.asmx?WSDL", # URL de homologación
            None,
            None,
            r"CERTIFICADOS\cacert.pem"
        )

        if not ok:
            raise RuntimeError(wsfev1.Excepcion)
        
        # obteniendo el TA para pruebas
        ta = InterfazWSAA().Crear_Ticket_Acceso_Firmado(
            service="wsfe",
            certificado=certificado_,
            clave=llave_,
            cuit=cuit_
        )
        wsfev1.SetTicketAcceso(ta)
        wsfev1.Cuit = cuit_

    def hacer_nota_credito(self, tipo_comprobante, punto_vta, nro_cbte):
        # comprobantes asociados (notas de crédito / débito)
        wsfev1.AgregarCmpAsoc(tipo_cbte = tipo_comprobante, punto_vta = punto_vta, nro_bte = nro_cbte)
    
    def facturar(self,datos_factura, datos_basicos_vendedor, tipo):
        
        fecha = datetime.datetime.now().strftime("%Y%m%d")
        
        cbte_nro = int(wsfev1.CompUltimoAutorizado(tipo, datos_basicos_vendedor["Punto_de_venta"]))
        
        moneda_id = "PES"
        moneda_ctz = "1.000" 
        cbt_desde = cbte_nro
        cbt_hasta = cbte_nro
        imp_tot_conc = "0.00"
        imp_iva = "0.00"
        imp_op_ex = "0.00"
        cancela_misma_moneda_ext='N'

        fecha_vto_pago = None
        fecha_servicio_desde = None
        fecha_servicio_hasta = None

        if int(datos_factura["ID_concepto"]) != 1:
            fecha_vto_pago = datos_factura["Fecha_vencimiento_de_pago"]
            fecha_servicio_desde = datos_factura["Fecha_servicio_desde"]
            fecha_servicio_hasta = datos_factura["Fecha_servicio_hasta"]

        wsfev1.CrearFactura(
            concepto=int(datos_factura["ID_concepto"]), # Concepto
            tipo_doc=int(datos_factura["ID_doc"]), # Tipo Documento
            nro_doc=str(datos_factura["Numero_de_documento_del_cliente"]), # Numero Documento
            tipo_cbte=int(tipo), # Tipo Comprobante
            punto_vta=int(datos_basicos_vendedor["Punto_de_venta"]), # Punto de Venta
            cbt_desde=cbt_desde + 1, # Comprobante desde
            cbt_hasta=cbt_hasta + 1, # Comprobante hasta
            imp_total=str(datos_factura["Importe_Total"]), # Importe total
            imp_tot_conc=imp_tot_conc, # Importe total conc
            imp_neto=str(datos_factura["Importe_Neto"]), # Importe Neto
            imp_iva=imp_iva, # Importe Iva
            imp_trib=str(datos_factura["Importe_Tributo"]), # Importe Tributo
            imp_op_ex=imp_op_ex, # Importe OP EX
            fecha_cbte=fecha, # Fecha comprobante
            fecha_venc_pago=fecha_vto_pago, # Fecha de vencimiento de pago
            fecha_serv_desde=fecha_servicio_desde, # Fecha de servicio desde
            fecha_serv_hasta=fecha_servicio_hasta, # Fecha de servicio hasta
            moneda_id=moneda_id, # ID moneda
            moneda_ctz=moneda_ctz, # Cotizacion moneda
            cancela_misma_moneda_ext=cancela_misma_moneda_ext,
            condicion_iva_receptor_id=datos_factura["ID_IVA_cliente"]
        )

        if tipo in (2, 3, 7, 8, 12, 13, 202, 203, 208, 213):
            self.hacer_nota_credito(
                datos_factura["nro_cbte_anular"],
                datos_basicos_vendedor["Punto_de_venta"],
                datos_factura["nro_cbte"]
            )
        
        tributo_factura_actual = datos_factura["tributos"]
        if len(tributo_factura_actual) > 0:
            for numero in range(len(tributo_factura_actual)):
                wsfev1.AgregarTributo(
                    int(tributo_factura_actual[numero][0]), # Tributo ID
                    str(tributo_factura_actual[numero][1]), # Descripcion
                    int(tributo_factura_actual[numero][2]), # Base Impositiva
                    int(tributo_factura_actual[numero][3]), # Alicuota
                    float(tributo_factura_actual[numero][4])  # Importe
                )  

        wsfev1.CAESolicitar()
        cae = wsfev1.CAESolicitar()

        print("Resultado", wsfev1.Resultado)
        print("Reproceso", wsfev1.Reproceso)
        print("CAE", cae)
        print("Vencimiento", wsfev1.Vencimiento)
        print("OBS", wsfev1.Obs)

        datosCAE=[wsfev1.CAE, wsfev1.Vencimiento, int(wsfev1.CompUltimoAutorizado(tipo, datos_basicos_vendedor["Punto_de_venta"]))]
        
        if datosCAE[0] == '':
            raise ErrorFacturacion(wsfev1.Obs)

        return datosCAE

if __name__ == '__main__':
    intWSFEv1 = InterfazWSFEv1()
    intWSFEv1.inicializar()
    intWSFEv1.facturar_prueba()