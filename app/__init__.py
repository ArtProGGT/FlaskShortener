from flask.app import Flask
from flask_sqlalchemy.extension import SQLAlchemy
app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)

from . import models, views

with app.app_context():
    db.create_all()
