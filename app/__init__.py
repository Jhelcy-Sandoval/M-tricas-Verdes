from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)


    # conexion a la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    db.init_app(app)

    #rutas de la app
    from . import routes
    routes.init_app(app)
    
    return app
