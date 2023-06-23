from flask import Flask, jsonify, request
from app import app, ma
from modelos import *

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'precio', 'stock', 'imagen')

# El objeto producto_schema es para traer un producto
producto_schema = ProductoSchema()
# El objeto productos_schema es para traer multiples registros de producto
productos_schema = ProductoSchema(many=True)
# crea los endpoint o rutas (json)

@app.route('/productos', methods=['GET'])
def get_Productos():
    # el metodo query.all() lo hereda de db.Model
    all_productos = Producto.query.all()
    # el metodo dump() lo hereda de ma.schema y
    result = productos_schema.dump(all_productos)
    # trae todos los registros de la tabla
    # retorna un JSON de todos los registros de la tabla
    return jsonify(result)

@app.route('/productos/<id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get(id)
    # retorna el JSON de un producto recibido como parametro
    return producto_schema.jsonify(producto)


@app.route('/productos/<id>', methods=['DELETE'])
def delete_producto(id):
    producto = Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    # me devuelve un json con el registro eliminado
    return producto_schema.jsonify(producto)

@app.route('/productos', methods=['POST'])  # crea ruta o endpoint
def create_producto():
    # print(request.json)  # request.json contiene el json que envio el cliente
    nombre = request.json['nombre']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']
    new_producto = Producto(nombre, precio, stock, imagen)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)

@app.route('/productos/<id>', methods=['PUT'])
def update_producto(id):
    producto = Producto.query.get(id)

    nombre = request.json['nombre']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']

    producto.nombre = nombre
    producto.precio = precio
    producto.stock = stock
    producto.imagen = imagen

    db.session.commit()
    return producto_schema.jsonify(producto)
