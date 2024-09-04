from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
  return render_template('index.html', title='Inicio', header='Bienvenido', content='Esto es Flask.')

@main.route('/home')
def home_page():
    return 'Welcome to the home page!'

def init_app(app):
    app.register_blueprint(main)