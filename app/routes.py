from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

# Simulación de "base de datos" en memoria
plants = [
    {
        'id': 1,
        'tag': 'PLANT001',
        'species': 'Aloe Vera',
        'germination_date': '2023-05-01',
        'initial_conditions': 'Suelo arenoso, baja humedad'
    },
    {
        'id': 2,
        'tag': 'PLANT002',
        'species': 'Cactus',
        'germination_date': '2023-06-15',
        'initial_conditions': 'Alta temperatura, baja humedad'
    },
]

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

    return render_template('datos-planta.html', title='datos-planta',  labels=labels, values=values, plantas=plants)

@main.route('/agregar-planta', methods=['POST'])
def agregar_planta():
    nueva_planta = {
        'id': len(plants) + 1,
        'tag': request.form['tag'],
        'species': request.form['species'],
        'germination_date': request.form['germination_date'],
        'initial_conditions': request.form['initial_conditions']
    }
    plants.append(nueva_planta)
    return redirect(url_for('main.datos_planta'))

# Ruta para eliminar una planta
@main.route('/eliminar-planta/<int:id>')
def eliminar_planta(id):
    global plants
    plants = [planta for planta in plants if planta['id'] != id]
    return redirect(url_for('main.datos_planta'))

def init_app(app):
    app.register_blueprint(main)