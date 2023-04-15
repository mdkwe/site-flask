from flask import Flask
 
from .views import app
from .models import db
 
#connect sqlalchemy to app
db.init_app(app)

@app.cli.command("init_db")
def init_db():
    models.init_db()