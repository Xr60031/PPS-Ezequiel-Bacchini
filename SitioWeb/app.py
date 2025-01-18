from flask import Flask
from flask import render_template, redirect, request, Response, session, make_response

app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
    saved_name = request.cookies.get("saved_name")
    return render_template('index.html', saved_name = saved_name)

@app.route('/save_name', methods=["POST"])
def save_name():
    name = request.form['name']
    response = make_response(f"Nos vamos a acordar de tu nombre, {name}!!!")
    response.set_cookie("saved_name", name)
    return response

@app.route('/delete_cookie')
def delete_cookie():
    response = make_response("Nos olvidamos de tu nombre!")
    response.set_cookie("saved_name", "", expires=0)
    return response

if __name__ == '__main__':
    app.secret_key="_Xr60031_"
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)