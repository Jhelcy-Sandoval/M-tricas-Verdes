import os
import json
from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

# Ruta del archivo db.json
DB_PATH = 'data/db.json'

# Función para leer los datos desde db.json
def leer_plantas():
    if not os.path.exists(DB_PATH):
        return []  # Si el archivo no existe, devolver una lista vacía
    # Se especifica la codificación 'utf-8' para leer el archivo
    with open(DB_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

# Función para escribir los datos en db.json
def guardar_plantas(plantas):
    # Crear la carpeta 'data' si no existe
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Guardar los datos en el archivo db.json
    with open(DB_PATH, 'w') as file:
        json.dump(plantas, file, indent=4)

plants = leer_plantas()


@main.route('/')
def home():
    return render_template('index.html', title='Métricas Verdes')

@main.route('/resumen')
def resumen():
    
    valuesh = [93, 95, 52, 48, 65, 66, 92, 65, 69, 53, 46, 55, 55, 74]
    labelsh = [
        "Valeriana", "Lupinus", "Calamagrostis", "Guantiva", "Dalea",
        "Gnaphalium", "Espeletia", "Hypericum", "Azorella", "Myrcianthes",
        "Pinguicula", "Bomarea", "Rubus", "Ranunculus"
    ]
    valuest = [22.5, 22.0, 16.7, 23.4, 10.3, 15.5, 15.8, 17.1, 23.2, 14.6, 18.9, 24.6, 16.0, 10.6, 12.8, 17.0, 24.3, 17.3, 22.7, 23.9]
    labelst = [
        "Frailejón", "Mortiño", "Senecio", "Chite", "Chuquiraga", 
        "Pernettya", "Valeriana", "Lupinus", "Calamagrostis", 
        "Guantiva", "Dalea", "Gnaphalium", "Espeletia", "Hypericum", 
        "Azorella", "Myrcianthes", "Pinguicula", "Bomarea", "Rubus", 
        "Ranunculus"
    ]
    labelsd = ["Frailejón", "Mortiño", "Senecio", "Chite", "Chuquiraga", "Pernettya", "Valeriana", "Lupinus", "Calamagrostis", "Guantiva", "Dalea", "Gnaphalium", "Espeletia", "Hypericum", "Azorella", "Myrcianthes", "Pinguicula", "Bomarea", "Rubus", "Ranunculus"]
    valuesd = [
        [55, 50, 2, 89, 72, 59, 35, 1, 46, 62, 90, 51],  # Frailejón
        [60, 33, 49],  # Mortiño
        [60, 43, 99, 37, 76, 11, 28, 57, 63, 97],  # Senecio
        [73, 81, 38, 10, 98, 2, 51, 1],  # Chite
        [41],  # Chuquiraga
        [59, 34, 9, 77, 65, 21, 83],  # Pernettya
        [100, 19, 9, 16, 12, 53, 79, 16, 26, 73],  # Valeriana
        [47, 89, 24, 100, 18, 37],  # Lupinus
        [32],  # Calamagrostis
        [71, 20, 91, 87, 50, 3, 16, 9, 73, 100, 32, 13],  # Guantiva
        [67, 64, 26, 83, 37],  # Dalea
        [41, 76, 91, 57, 47, 100, 50, 89, 68],  # Gnaphalium
        [28, 62, 45, 50, 12, 30, 17, 34, 70, 29, 66],  # Espeletia
        [83, 85, 49],  # Hypericum
        [15, 95, 85, 82, 93, 10, 71, 85, 34],  # Azorella
        [100, 50, 27, 69, 33, 35],  # Myrcianthes
        [71, 3, 82, 69, 22, 45, 41, 76, 71, 82],  # Pinguicula
        [16, 92, 14, 63, 78, 54, 32, 79],  # Bomarea
        [25, 26, 66, 94, 29, 51, 20],  # Rubus
        [91, 22, 7, 12]  # Ranunculus
    ]

    labels_stat = ["Temperatura", "Humedad", "Desarrollo"]
    values_stat = [
        [22.5, 22.0, 16.7, 23.4, 10.3, 15.5, 15.8, 17.1, 23.2, 14.6, 18.9, 24.6, 16.0, 10.6, 12.8, 17.0, 24.3, 17.3, 22.7, 23.9], 
        [85, 78, 90, 88, 82, 77, 83, 85, 80, 75, 79, 81],  
        [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]  
    ]
    return render_template('resumen.html', 
        title='Dashboard', 
        valuesh=valuesh, 
        labelsh=labelsh, 
        valuest=valuest, 
        labelst=labelst, 
        labelsd=labelsd, 
        valuesd=valuesd,
        labels_stat=labels_stat, 
        values_stat=values_stat 
    )

@main.route('/datos-planta')
def datos_planta():
    labels = ['January', 'February', 'March', 'April', 'May', 'June']
    values = [10, 20, 30, 40, 50, 60]

    plantas = leer_plantas()

    return render_template('datos-planta.html', title='Datos Planta', labels=labels, values=values, plantas=plantas)

@main.route('/alertas')
def alertas():
    return render_template('alertas.html', title='alertas')

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

    # Guardar las plantas actualizadas en el archivo
    guardar_plantas(plantas)

    return redirect(url_for('main.datos_planta'))

@main.route('/eliminar-planta/<int:id>')
def eliminar_planta(id):

    plantas = leer_plantas()

    # Filtrar la planta a eliminar
    plantas = [planta for planta in plantas if planta['id'] != id]

    # Guardar los cambios en el archivo
    guardar_plantas(plantas)

    return redirect(url_for('main.datos_planta'))
    
def init_app(app):
    app.register_blueprint(main)
