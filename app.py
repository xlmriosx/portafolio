from flask import Flask, escape, request, url_for, render_template, jsonify, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



#
# @app.route('/login', methods=['get','POST'])
# def login():
#     if request.method=='POST':
#         # No valido aun
#         usuario = request.form['username']
#         #agrego al usuario a la sesion
#         session['username']= usuario
#         return redirect(url_for('hello'))
#     return render_template('login.html')
#
# @app.route('/logout')
# def logout():
#     session.pop('username')
#     return redirect(url_for('hello'))
#
# @app.route('/saludar/<nombre>')
# def saludar(nombre):
#     return f'Holaaa {nombre}'
#
# @app.route('/edad/<int:edad>')
# def mostrar_edad(edad):
#     return f'Tu edad es: {edad}'
#
# @app.route('/mostrar/<nombre>', methods=['get', 'post'])
# def mostrar_nombre(nombre):
#     return render_template('mostrar.html', nombre=nombre)
#
# @app.route('/redireccionar')
# def redireccionar():
#     return redirect(url_for('hello'))
#
# @app.route('/salir')
# def salir():
#     return abort(404)
#
# @app.errorhandler(404)
# def pagina_no_encontrada(error):
#     return render_template('error404.html', error=error), 404
#
#
# #ReST - Representational State Transfer
# @app.route('/api/mostrar/<nombre>', methods=['post','get'])
# def mostrar_json(nombre):
#     valores = {'nombre': nombre, 'metodo': request.method}
#     return jsonify(valores)
