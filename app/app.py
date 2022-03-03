from datetime import datetime
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

from config import Config
from validation import validation_errors

from json import dumps


load_dotenv('./.env')

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
from models import Record


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.headers.get('X-Requested_With') == 'XMLHttpRequest':
        page, order_by, sort, filter = request.get_json().values()
        limit = 10
        offset = limit * (page - 1)
        records_count = Record.query.count()
        pages_count = (records_count // limit) + 1
        if sort == 'asc':
            records = Record.query.order_by(order_by).offset(offset).limit(limit).all()
        else:
            records = Record.query.order_by(desc(order_by)).offset(offset).limit(limit).all()
        res = {
            'pages_count': pages_count,
            'records': records
            }
        return jsonify(res)
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create_record():
    input = request.get_json()
    errors = validation_errors(input)
    if not errors:
        record = Record(
            title = input['title'],
            date = datetime.strptime(input['date'], "%Y-%m-%d"),
            amount = input['amount'],
            distance = input['distance']
        )

        db.session.add(record)
        db.session.commit()

        return '', 204
    return jsonify(errors)


if __name__ == '__main__':
    app.run()