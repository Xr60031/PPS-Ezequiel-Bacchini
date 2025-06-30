from flask import Flask, send_file, render_template, request, make_response, redirect, url_for, Response, session, flash, jsonify

from Facades.facade_google_apis import Facade_API_google
from Facades.facade_facturacion import Facade_facturacion
from Facades.facade_json import Facade_Json
from Facades.facade_usuario import Facade_usuario_manager
from Facades.facade_datos_factura import Facade_datos_factura
from Facades.facade_dataframes import Facade_dataframe
from Facades.facade_configuracion import Facade_Configuracion
from Facades.facade_items import Facade_Items
from Facades.facade_historial import Facade_Historial

from Funciones.Obtener_datos_facturacion.obtenedor_FM import Obtenedor_FM
from Funciones.Obtener_datos_facturacion.obtenedor_FU import Obtenedor_FU
from Funciones.Obtener_datos_facturacion.obtenedor_NC import Obtenedor_NC

from Funciones.Verificadores.verificador_CUIT import Verificador_CUIT
from Funciones.Verificadores.verificar_formateo_datos import Verificador_Formateo_Datos_Facturacion
from Funciones.Verificadores.verificador_inicio_sesion import Verificador_Inicio_Sesion

import interfaz_wsaa
from Constantes import constantes

import os
import shutil
from threading import Thread
import threading
import time
import re
from datetime import datetime, timedelta

import traceback
from Exceptions.Exceptions_Custom.exception_error_factura import ErrorFacturacion

app = Flask(__name__)
app.secret_key = 'clave_030'
WSAA = interfaz_wsaa.InterfazWSAA()
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.permanent_session_lifetime = timedelta(days=365 * 100)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

configuracion = Facade_Configuracion()
items_manager = Facade_Items()
historial = Facade_Historial()
API_Google = Facade_API_google()
facturador = Facade_facturacion()
json = Facade_Json()
constantes_ = constantes

# ELIMINA UN ARCHIVO EN LA RUTA ESPECIFICADA
def delete_file_after_download(file_path):
    time.sleep(constantes_.sleep_time)
    os.remove(file_path)

def delete_file_after_download_extended(file_path):
    time.sleep(constantes_.sleep_time_extended)
    os.remove(file_path)

@app.route('/')
def root():
    session['llave_exitosa'] = False
    return redirect(url_for('index'))

# RENDERIZA EL MENU PRINCIPAL
@app.route('/index')
def index():
    session.permanent = True
    return render_template('index.html')

# RENDERIZA LA PAGINA PARA INICIAR SESION
@app.route('/inicio_sesion')
def inicio_sesion():
    if 'configuracion_inicial' not in session:
        session['configuracion_inicial'] = False
    return render_template('IniciarSesion.html')

# RENDERIZA LA PAGINA PARA CREAR LA CUENTA
@app.route('/crear_cuenta')
def crear_cuenta():
    return render_template('CrearCuenta.html')

# RENDERIZA LA PAGINA PARA OBTENER AYUDA
@app.route('/config')
def config():
    return render_template('Configuracion.html')

# RENDERIZA LA PAGINA PARA OBTENER AYUDA
@app.route('/ayuda')
def ayuda():
    return render_template('Ayuda.html')

# RENDERIZA LA PAGINA PARA
@app.route('/informacion_cookies')
def informacion_cookies():
    return render_template('Informacion_cookies_extra.html')

# RENDERIZA LA PAGINA PARA OBTENER AYUDA
@app.route('/documentacion')
def documentacion():
    return render_template('Documentacion.html')

# RENDERIZA LA PAGINA PARA OBTENER AYUDA
@app.route('/sis_info')
def sis_info():
    return render_template('Sobre_el_sistema.html')

# RENDERIZA EL MENU DE FACTURACION
@app.route('/menu_facturador', methods=['GET','POST'])
def menu_facturador():
    return render_template('FacturadorMenu.html')

# RENDERIZA EL MENU DE FACTURACION DESDE ALGUNO DE LOS MENUS DE FACTURACIÓN O HISTORIAL
# Elimina el Excel del repositorio en Drive
@app.route('/menu_facturador_')
def menu_facturador_():
    API_Google.delete_drive(session.get('excelID'))
    return render_template('FacturadorMenu.html')

# RENDERIZA EL MENU QUE TIENE LAS DEFINICIONES DEL PROCESO DE FACTURACIÓN
@app.route('/definiciones_facturacion', methods=['GET'])
def definiciones_facturacion():
    return render_template('Definiciones_Facturacion.html')

# RENDERIZA EL MENU PRINCIPAL
# Elimina el Excel del repositorio en Drive
@app.route('/index_')
def index_():
    API_Google.delete_drive(session.get('excelID'))
    session.permanent = True
    return render_template('index.html')

# RENDERIZA EL MENÚ PARA CONFIGURAR ITEMS
@app.route('/menu_items')
def menu_items():
    destination_path = API_Google.descargar_excel(constantes_.excel_sin_borrado_de_drive, session.get('excelID'), session.get('excel_name'))
    items = items_manager.obtener_productos_servicios(destination_path)
    Thread(target=delete_file_after_download, args=(destination_path,)).start()
    return render_template('ProductoServicio.html', items = items)

# AGREGA UN ITEM (PRODCUTO O SERVICIO) A LA PLANTILLA
@app.route('/agregar_item', methods=['GET','POST'])
def agregar_item():
    datos = []
    datos.append(request.form.get("prod_ser"))
    datos.append(request.form.get("codigo_prod_ser") or None)
    datos.append(request.form.get("desc") or None)
    datos.append(int(request.form.get("precio")))
    datos.append(request.form.get("concepto") or None)
    datos.append(request.form.get("d_i_a") or None)
    datos.append(request.form.get("alicuota") or None)

    destination_path = API_Google.descargar_excel(constantes_.excel_con_borrado_de_drive, session.get('excelID'), session.get('excel_name'))
    items_manager.agregar_producto_servicio(path_excel=destination_path, datos=datos)
    items = items_manager.obtener_productos_servicios(destination_path)

    embed_1_excel_id_0 = API_Google.subir_excel(destination_path, session.get('excel_name'))
    session['excelID'] = embed_1_excel_id_0[0]
    session['embed'] = embed_1_excel_id_0[1]
    

    Thread(target=delete_file_after_download, args=(destination_path,)).start()
    flash(constantes_.mensaje_accion_item("AGREGADO"))

    return render_template('ProductoServicio.html', items = items)

# MODIFICA UN ITEM (PRODUCTO O SERVICIO) DE LA PLANTILLA
@app.route('/modificar_item', methods=['GET','POST'])
def modificar_item():
    datos = []
    datos.append(request.form.get("prod_ser") or None)
    datos.append(request.form.get("codigo_prod_ser") or None)
    datos.append(request.form.get("desc") or None)
    datos.append(request.form.get("precio") or None)
    datos.append(request.form.get("concepto") or None)
    datos.append(request.form.get("d_i_a") or None)
    datos.append(request.form.get("alicuota") or None)
    selected_item = request.form.get("selected_item")

    destination_path = API_Google.descargar_excel(constantes_.excel_con_borrado_de_drive, session.get('excelID'), session.get('excel_name'))

    items_manager.modificar_producto_servicio(destination_path, datos, selected_item)

    items = items_manager.obtener_productos_servicios(destination_path)

    embed_1_excel_id_0 = API_Google.subir_excel(destination_path, session.get('excel_name'))
    
    session['excelID'] = embed_1_excel_id_0[0]
    session['embed'] = embed_1_excel_id_0[1]

    Thread(target=delete_file_after_download, args=(destination_path,)).start()

    flash(constantes_.mensaje_accion_item("MODIFICADO"))
    
    return render_template('ProductoServicio.html', items = items)

# ELIMINA UN ITEM (PRODUCTO O SERVICIO) DE LA PLANTILLA
@app.route('/eliminar_item', methods=['GET','POST'])
def eliminar_item():
    selected_item = request.form.get("selected_item")

    destination_path = API_Google.descargar_excel(constantes_.excel_con_borrado_de_drive, session.get('excelID'), session.get('excel_name'))

    items_manager.eliminar_producto_servicio(destination_path, selected_item)

    items = items_manager.obtener_productos_servicios(destination_path)

    embed_1_excel_id_0 = API_Google.subir_excel(destination_path, session.get('excel_name'))
    
    session['excelID'] = embed_1_excel_id_0[0]
    session['embed'] = embed_1_excel_id_0[1]

    Thread(target=delete_file_after_download, args=(destination_path,)).start()

    flash(constantes_.mensaje_accion_item("ELIMINADO"))
    
    return render_template('ProductoServicio.html', items = items)

@app.route('/descargar_archivo_excel', methods=['GET', 'POST'])
def descargar_archivo_excel():
    destination_path = API_Google.descargar_excel(constantes_.excel_sin_borrado_de_drive, session.get('excelID'), session.get('excel_name'))
    Thread(target=delete_file_after_download_extended, args=(destination_path,)).start()
    return make_response(send_file(destination_path, as_attachment=True, download_name = constantes_.excel_name(session.get('CUIT'))))

# CARGA EL  FACTURADOR UNICO O EL FACTURADOR MULTIPLE EN BASE A LA ACCION REALIZADA POR EL USUARIO
# ADICIONALMENTE SE ENCARGA DE SUBIR AL DRIVE LA PLANTILLA DE FACTURACION PARA PODER SER UTILIZADA DESDE EL SITIO
@app.route('/load_facturador', methods=['GET', 'POST'])
def load_facturador():
    excel = request.files.get("excel")
    action = request.form.get("accion")

    if excel.filename != f"Plantilla_{session.get('CUIT')}_.xlsx" and not re.match(rf"^Plantilla_{session.get('CUIT')}_\((\d+)\)\.xlsx$", excel.filename):
        flash(constantes_.excel_no_valido_alerta)
        return redirect(url_for('menu_facturador'))
    
    path_excel = os.path.join(app.config["UPLOAD_FOLDER"], excel.filename)
    excel.save(path_excel)
    session['excel_name'] = excel.filename
    embed_1_excel_id_0 = API_Google.subir_excel(path_excel, session.get('excel_name'))
    
    session['excelID'] = embed_1_excel_id_0[0]
    session['embed'] = embed_1_excel_id_0[1]

    if action == "f_unico":
        items = items_manager.obtener_productos_servicios(path_excel)
        Thread(target=delete_file_after_download, args=(path_excel,)).start()
        return render_template('FacturadorUnico.html', items=items, estado = session.get('descargar_excel'))
    elif action == "f_multiple":
        Thread(target=delete_file_after_download, args=(path_excel,)).start()
        return render_template('FacturadorMultiple.html', embed_link=session.get('embed'), estado = session.get('descargar_excel'))
    elif action == "menu_items":
        items = items_manager.obtener_productos_servicios(path_excel)
        Thread(target=delete_file_after_download, args=(path_excel,)).start()
        return render_template('ProductoServicio.html', items = items)
    elif action == "historial":
        historial_ = historial.obtener_historial(path_excel)
        Thread(target=delete_file_after_download, args=(path_excel,)).start()
        return render_template('Historial.html', historial = historial_)

def escribir_certificado():
    certificado_name = constantes_.get_certificado_name(session.get('CUIT'))
    copy_path_certificado = constantes_.get_upload_path(certificado_name)
    contenido_certificado = session.get('certificado')

    with open(copy_path_certificado, "w", newline='') as file:
        file.write(contenido_certificado)
    
    return copy_path_certificado

def escribir_llave():
    llave_name = constantes_.get_llave_privada_name(session.get('CUIT'))
    copy_path_llave = constantes_.get_upload_path(llave_name)
    contenido_llave = session.get('llave_privada')
    
    with open(copy_path_llave, "w") as file:
        file.write(contenido_llave)

    return copy_path_llave

# REALIZA LA FACTURACION DE UNA FACTURA
@app.route('/facturacion', methods=['GET','POST'])
def facturacion():
    modo_factura = request.form.get("modo_facturacion")

    destination_path = API_Google.descargar_excel(constantes_.excel_con_borrado_de_drive, session.get('excelID'), session.get('excel_name'))
    
    datos_factura_manager = Facade_datos_factura()
    dataframe_manager = Facade_dataframe()
    usuario_manager = Facade_usuario_manager()

    datos_usuario = usuario_manager.obtener_datos_usuario(destination_path)
    datos_usuario = usuario_manager.armar_biblioteca_vendedor(datos_usuario)
    data_source = None

    if(modo_factura == "Factura Unico"):
        data_source = request
        obtenedor = Obtenedor_FU()
    elif (modo_factura == "Factura Multiple"):
        data_source = destination_path
        obtenedor = Obtenedor_FM()
    elif (modo_factura == "Nota Credito"):
        data_source = request.form.get("selected_items_json")
        obtenedor = Obtenedor_NC()
    
    try:
        datos_factura = obtenedor.obtener_datos_facturacion(data_source, datos_factura_manager, datos_usuario)
    except Exception as e:
        path_log = 'Exceptions/log_exceptions.txt'
        with open(path_log, 'a', encoding='utf-8') as file:
            file.write("\n")
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            file.write(" " + str(e))
            file.write(" " + traceback.format_exc())
        flash(constantes.algo_salio_mal_alerta)
        return render_template('FacturadorMenu.html')

    if isinstance(datos_factura, dict):
        datos_factura = [datos_factura]

    verificador_formateo_datos_facturacion = Verificador_Formateo_Datos_Facturacion()
    for datos_actual in datos_factura:
        if(verificador_formateo_datos_facturacion.verificar_formateo_datos(datos_actual) == False):
            flash(constantes_.factura_datos_faltantes_alerta)
            return render_template('FacturadorMenu.html')

    copy_path_certificado = escribir_certificado()
    copy_path_llave = escribir_llave()

    if not session.get('ticket_tiempo_creacion'):
        session['ticket_creado'] = False
    else:
        creacion = datetime.fromisoformat(session.get('ticket_tiempo_creacion'))
        session['ticket_creado'] = not (datetime.now() > creacion + timedelta(hours=2))

    if session.get('ticket_creado'):
        ticket_content = dataframe_manager.obtener_xml(destination_path)
        file_path = os.path.join('uploads', f'Ticket_Acceso{session.get('CUIT')}.xml')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(ticket_content)

    dataframe_historial = dataframe_manager.obtener_dataframe_historial(destination_path)
    
    try:
        zip_file = facturador.facturacion(destination_path, copy_path_llave, copy_path_certificado, datos_usuario, datos_factura, dataframe_historial)
    except ErrorFacturacion as e:
        flash(str(e.mensaje))
        return render_template('FacturadorMenu.html')
    except Exception as e:
        path_log = 'Exceptions/log_exceptions.txt'
        with open(path_log, 'a', encoding='utf-8') as file:
            file.write("\n")
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            file.write(" " + str(e))
            file.write(" " + traceback.format_exc())
        flash(constantes.algo_salio_mal_alerta)
        return render_template('FacturadorMenu.html')

    session['ticket_creado'] = True
    session['ticket_tiempo_creacion'] = datetime.now().isoformat()

    Thread(target=delete_file_after_download, args=(copy_path_llave,)).start()
    Thread(target=delete_file_after_download, args=(copy_path_certificado,)).start()
    Thread(target=delete_file_after_download, args=(destination_path,)).start()
    Thread(target=delete_file_after_download, args=(f"uploads/Ticket_Acceso{session.get('CUIT')}.xml",)).start()

    zip_file.seek(0)

    return make_response(send_file(zip_file, as_attachment=True, download_name=constantes_.zip_name(session.get('CUIT'), datetime.now(), modo_factura)))

# GENERA EL ARCHIVO DE LA LLAVE PRIVADA Y LO DESCARGA
@app.route('/hacer_llave', methods=['POST'])
def hacer_llave():
    verificador_cuit = Verificador_CUIT()
    CUIT= request.form['CUIT']
    if verificador_cuit.verificar_cuit(CUIT) == False:
        flash(constantes_.cuit_no_valido_alerta)
        return render_template('CrearCuenta.html')
    
    clave = WSAA.Crear_Llave_Privada(CUIT)
    session['llave_exitosa'] = True
    response =make_response(Response(
        clave[0],
        mimetype="text/plain",
        headers={"Content-Disposition": f"attachment; filename={clave[1]}"}
    ))
    
    session['CUIT'] = CUIT
    
    return response

# GENERA EL ARCHIVO PARA REALIZAR EL PEDIDO DE CERTIFICADO Y LO DESCARGA
@app.route('/hacer_pedido_certificado', methods=['POST'])
def hacer_pedido_certificado():

    # Verificar si la primera función fue exitosa
    if not session.get('llave_exitosa', False):
        flash(constantes_.llave_no_generada_alerta)
        return render_template('CrearCuenta.html')

    CUIT= session.get('CUIT')
    NOMBRE= request.form['Nombre']
    EMPRESA= request.form['Empresa']

    pedido = WSAA.Crear_Pedido_Certificado(CUIT, NOMBRE, EMPRESA)
    session['Nombre'] = NOMBRE
    session['Empresa'] = EMPRESA
    
    return make_response(Response(
        pedido[0],
        mimetype="text/plain",
        headers={"Content-Disposition": f"attachment; filename={pedido[1]}"}
    ))

# BORRA LOS MENSAJES FLASH GENERADOS EN EL SITIO
@app.route('/delete_message', methods=['POST'])
def delete_message():
    session.pop('_flashes', None)
    return jsonify(success=True)

# GUARDA LA LLAVE Y EL CERTIFICADO COMO SESSION COOKIES Y RENDERIZA EL MENU O LAS CONFIGURACIONES
# EN BASE A SI YA SE CONFIGURÓ EL SITIO POR PRIMERA VEZ
@app.route('/upload', methods=['POST'])
def upload_file():
    verificador_inicio_sesion = Verificador_Inicio_Sesion()
    try:
        llave = request.files.get('llave')
        llave_legible = llave.read().decode('utf-8')
        certificado = request.files.get('certificado')
        certificado_legible = certificado.read().decode('utf-8')

        if not verificador_inicio_sesion.leer_certificado(certificado_legible) or not verificador_inicio_sesion.leer_llave(llave_legible):
            flash(constantes_.llave_certificado_no_validos_alerta)
            return redirect(url_for('inicio_sesion'))
        
        session['llave_privada'] = llave_legible
        session['certificado'] = certificado_legible

        if(session.get('configuracion_inicial') == True):
            return render_template('FacturadorMenu.html')
        else:
            requiere_datos_adicionales = session.get('CUIT')==None or session.get('Nombre')==None or session.get('Empresa') == None
            return render_template('Configuracion_Inicial.html', requiere_datos_adicionales = requiere_datos_adicionales)
    
    except Exception as e:
        flash(f"Error al procesar los archivos", "error")
        return redirect(url_for('inicio_sesion'))

# FUNCIONES DE CONFIGURACION DE CUENTA
# GUARDA LAS CONFIGURACIONES
@app.route('/save_configuracion', methods=['POST'])
def save_configuracion():
    excel = request.files.get("excel")

    if excel.filename != f"Plantilla_{session.get('CUIT')}_.xlsx" and not re.match(rf"^Plantilla_{session.get('CUIT')}_\((\d+)\)\.xlsx$", excel.filename):
        flash(constantes_.excel_no_valido_alerta)
        return redirect(url_for('config'))

    config = [
        request.form['name'],
        request.form['CUIT'],
        request.form['empresa'],
        request.form['pventa'],
        request.form['razonsocial'],
        request.form['domicilio'],
        request.form['condicionIVA'],
        request.form['ingresosbrutos'],
        request.form['fechaInicio'],
        request.form['iag'],
        request.form['d_iag'],
        request.form['alicuota']
    ]
    
    path_excel = os.path.join(app.config["UPLOAD_FOLDER"], excel.filename)
    excel.save(path_excel)
    session['excel_name'] = excel.filename

    configuracion.guardar_configuracion(path_excel, config)
    Thread(target=delete_file_after_download, args=(path_excel,)).start()

    return make_response(send_file(path_excel, as_attachment=True, download_name = constantes_.excel_name(session.get('CUIT'))))

@app.route('/get_filename')
def get_filename():
    output_file_name = constantes_.excel_name(session.get('CUIT'))
    return jsonify({"filename": output_file_name})

# GUARDA LA CONFIGURACION INICIAL DEL SISTEMA PARA LA PLANTILLA
@app.route('/save_configuracion_inicial', methods=["POST"])
def save_configuracion_inicial():
    config = [
        request.form['nombre_apellido'] if request.form.get('nombre_apellido') else session.get('Nombre'),
        request.form['CUIT'] if request.form.get('CUIT') else session.get('CUIT'),
        request.form['nombre_empresa'] if request.form.get('nombre_empresa') else session.get('Empresa'),
        request.form['pventa'],
        request.form['razonsocial'],
        request.form['domicilio'],
        request.form['condicionIVA'],
        request.form['ingresosbrutos'],
        request.form['fecha_inicio'],
        request.form['iag'],
        request.form['d_iag'],
        request.form['alicuota']
    ]

    if session.get('CUIT') == None:
        session['CUIT'] = request.form['CUIT']
    
    output_file_name = constantes_.excel_name(config[1])
    copy_path = constantes_.get_copy_path(output_file_name)

    template_path = constantes_.excel_template_path
    shutil.copy(template_path, copy_path)

    configuracion.guardar_configuracion_inicial(template_path,config,copy_path)
    session['configuracion_inicial']= True
    Thread(target=delete_file_after_download, args=(copy_path,)).start()

    return make_response(send_file(copy_path, as_attachment=True))

#FUNCIONES DE MANEJO DE DATOS CERRAR / VOLVER A ABRIR SESION
def eliminar_archivo():
    time.sleep(5)
    os.remove('session_data.json')

def default_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return str(obj)

@app.route('/borrar_sesion', methods=['POST'])
def borrar_sesion():
    session_data = dict(session)
    with open('session_data.json', 'w') as file:
        json.dump(session_data, file, default_serializer)

    response = send_file('session_data.json', as_attachment=True)

    session['configuracion_inicial'] = False
    session['Nombre'] = None
    session['Empresa'] = None
    session['CUIT'] = None
    session['llave_exitosa'] = False
    session['llave_privada'] = None
    session['certificado'] = None
    session['excelID'] = None
    session['excel_name'] = None
    session['embed'] = None
    session['ticket_creado'] = False
    session['ticket_tiempo_creacion'] = None

    response.set_cookie("cookies_aceptadas", "", expires=0)

    thread = Thread(target=eliminar_archivo)
    thread.start()

    return response

EXPIRATION_MINUTES = 10
CLEANUP_INTERVAL_SECONDS = 300  # cada 5 minutos

def cleanup_old_files():
    while True:
        try:
            now = datetime.now()
            for filename in os.listdir(UPLOAD_FOLDER):
                path = os.path.join(UPLOAD_FOLDER, filename)
                if os.path.isfile(path):
                    modified_time = datetime.fromtimestamp(os.path.getmtime(path))
                    if now - modified_time > timedelta(minutes=EXPIRATION_MINUTES):
                        os.remove(path)
                        print(f"Archivo eliminado: {path}")
        except Exception as e:
            print(f"[Error de limpieza]: {e}")
        time.sleep(CLEANUP_INTERVAL_SECONDS)

def start_cleanup_thread():
    thread = threading.Thread(target=cleanup_old_files, daemon=True)
    thread.start()

if __name__ == '__main__':
    app.secret_key = "_Xr60031_"
    start_cleanup_thread()
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)