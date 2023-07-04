from app import db, app

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