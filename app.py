from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

# Configurar la base de datos
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mbdev:Pruebas132@mbdev.mysql.pythonanywhere-services.com/mbdev$default'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/proyecto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define las rutas utilizando el controlador de usuario

@app.route('/')
def hello():
    return jsonify(message='¡Hola mundo!')

#Comentar en pythonanywhere
from controllers.usuario_controller import *

# Descomentar en pythonanywhere 
"""
from controllers import usuario_controller
app.route('/usuarios', methods=['GET'])(usuario_controller.get_usuarios)
app.route('/usuarios/<id>', methods=['GET'])(usuario_controller.get_usuario)
app.route('/usuarios/<id>', methods=['DELETE'])(usuario_controller.delete_usuario)
app.route('/usuarios', methods=['POST'])(usuario_controller.create_usuario)
app.route('/usuarios/<id>', methods=['PUT'])(usuario_controller.update_usuario)
"""

# programa principal, comentar en pythonanywhere
if __name__ == '__main__':
    # ejecuta el servidor Flask en el puerto 5000
    app.run(debug=True, port=5000)
