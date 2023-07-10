from app import app, db
from models.usuario_model import Usuario, UsuarioSchema
from flask import jsonify, request
import os
app.config['UPLOAD_FOLDER'] = '/img'

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    all_usuarios = Usuario.query.all()
    result = usuarios_schema.dump(all_usuarios)
    return jsonify(result)

@app.route('/usuarios/<id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get(id)
    return usuario_schema.jsonify(usuario)

@app.route('/usuarios/<id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return usuario_schema.jsonify(usuario)

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    direccion = request.json['direccion']
 
    new_usuario = Usuario(nombre=nombre, apellido=apellido, direccion=direccion)
    db.session.add(new_usuario)
    db.session.commit()
    return usuario_schema.jsonify(new_usuario)

@app.route('/usuarios/<id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario is None:
        return jsonify({'message': 'Usuario no encontrado'})
    usuario.nombre = request.json['nombre']
    usuario.apellido = request.json['apellido']
    usuario.direccion = request.json['direccion']
    db.session.commit()
    return usuario_schema.jsonify(usuario)
