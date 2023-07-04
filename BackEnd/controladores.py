from flask import Flask, jsonify, request
from app import ma
from modelos import *

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
