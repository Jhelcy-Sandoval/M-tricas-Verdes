from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# esquema de los datos de la planta
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(100), unique=True, nullable=False)
    species = db.Column(db.String(100), nullable=False)
    germination_date = db.Column(db.DateTime, nullable=False)
    initial_conditions = db.Column(db.String(200))
