import json
from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

# Simulación de "base de datos" en memoria
DB_PATH = 'data/db.json'

def leer_plantas():
    try:
        with open(DB_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Función para escribir los datos en db.json
def guardar_plantas(plantas):
    with open(DB_PATH, 'w') as file:
        json.dump(plantas, file, indent=4)

# Leer las plantas desde el archivo al iniciar la aplicación
plants = leer_plantas()

@main.route('/')
def home():
  return render_template('index.html', title='Metricas verdes')

@main.route('/resumen')
def resumen():
    return render_template('resumen.html', title='Dashboard')

@main.route('/datos-planta')
def datos_planta():

    labels = ['January', 'February', 'March', 'April', 'May', 'June']
    values = [10, 20, 30, 40, 50, 60]

    plantas = leer_plantas()

    return render_template('datos-planta.html', title='datos-planta',  labels=labels, values=values, plantas=plants)

@main.route('/agregar-planta', methods=['POST'])
def agregar_planta():
    plantas = leer_plantas()

    nueva_planta = {
        'id': len(plantas) + 1,
        'tag': request.form['tag'],
        'species': request.form['species'],
        'germination_date': request.form['germination_date'],
        'initial_conditions': request.form['initial_conditions']
    }
    plantas.append(nueva_planta)

    guardar_plantas(plantas)

    return redirect(url_for('main.datos_planta'))

# Ruta para eliminar una planta
@main.route('/eliminar-planta/<int:id>')
def eliminar_planta(id):
    global plants
    plants = [planta for planta in plants if planta['id'] != id]
    return redirect(url_for('main.datos_planta'))

def init_app(app):
    app.register_blueprint(main)