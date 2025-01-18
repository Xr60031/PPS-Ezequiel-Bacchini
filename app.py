from flask import Flask
from flask import render_template, redirect, request, Response, session

app = Flask(__name__,template_folder='FACTURADOR-ELECTRONICO-AFIP-ARCA')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/accesso-login', methods=["GET", "POST"])
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key="_Xr60031_"
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)