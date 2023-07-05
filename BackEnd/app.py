from flask import Flask, jsonify, request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app)  # modulo cors es para que me permita acceder desde el frontend al backend

# configuro la base de datos, con el nombre el usuario y la clave
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mbdev:Pruebas132@mbdev.mysql.pythonanywhere-services.com/mbdev$default'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/proyecto'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # none
db = SQLAlchemy(app)  # crea el objeto db de la clase SQLAlquemy
ma = Marshmallow(app)  # crea el objeto ma de de la clase Marshmallow


# defino la tabla
class Usuario(db.Model):   # la clase Usuario hereda de db.Model
    # define los campos de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    direccion = db.Column(db.String(100))

    def __init__(self, nombre, apellido, direccion):  # crea el  constructor de la clase
        # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion

with app.app_context():
    db.create_all()  # aqui crea todas las tablas

#  ************************************************************
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'apellido', 'direccion')

# El objeto usuario_schema es para traer un usuario
usuario_schema = UsuarioSchema()
# El objeto usuarios_schema es para traer multiples registros de usuario
usuarios_schema = UsuarioSchema(many=True)
# crea los endpoint o rutas (json)

@app.route('/usuarios', methods=['GET'])
def get_Usuarios():
    # el metodo query.all() lo hereda de db.Model
    all_usuarios = Usuario.query.all()
    # el metodo dump() lo hereda de ma.schema y
    result = usuarios_schema.dump(all_usuarios)
    # trae todos los registros de la tabla
    # retorna un JSON de todos los registros de la tabla
    return jsonify(result)

@app.route('/usuarios/<id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get(id)
    # retorna el JSON de un usuario recibido como parametro
    return usuario_schema.jsonify(usuario)


@app.route('/usuarios/<id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    # me devuelve un json con el registro eliminado
    return usuario_schema.jsonify(usuario)

@app.route('/usuarios', methods=['POST'])  # crea ruta o endpoint
def create_usuario():
    # print(request.json)  # request.json contiene el json que envio el cliente
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    direccion = request.json['direccion']
    new_usuario = Usuario(nombre, apellido, direccion)
    db.session.add(new_usuario)
    db.session.commit()
    return usuario_schema.jsonify(new_usuario)

@app.route('/usuarios/<id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get(id)

    nombre = request.json['nombre']
    apellido = request.json['apellido']
    direccion = request.json['direccion']

    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.direccion = direccion

    db.session.commit()
    return usuario_schema.jsonify(usuario)

if __name__=='__main__':
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000


