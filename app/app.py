from crypt import methods
from pyexpat import model
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from config import Config


load_dotenv('./.env')

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
import models

@app.route('/')
def index():
    if request.headers.get('X-Requested_With') == 'XMLHttpRequest':
        records = jsonify(models.Record.query.all())
        return records
    return render_template('index.html')


@app.route('create', methods=['POST'])
def create_record():
    user_input = request.get_json()


if __name__ == '__main__':
    app.run()