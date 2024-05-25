from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def status():
    return {
        "status": "success",
        "message": "Welcome to the Energy Reports API"
    }
