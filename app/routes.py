from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
  return render_template('index.html', title='Metricas verdes')

@main.route('/resumen')
def resumen():
    return render_template('resumen.html', title='Dashboard')

@main.route('/datos-planta')
def datos_planta():
    return render_template('datos-planta.html', title='datos-planta')

def init_app(app):
    app.register_blueprint(main)