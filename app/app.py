import operator
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

from config import Config
from validation import create_validation, filter_validation

from json import dumps


load_dotenv('./.env')

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
from models import Record


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.headers.get('X-Requested_With') == 'XMLHttpRequest':
        req = request.get_json()
        page = req['page']
        order_by = req['order_by']
        sort = req['sort']
        filter = req['filter']

        limit = 10
        offset = limit * (page - 1)

        res = {'errors': ''}

        query = Record.query
        if all(filter.values()):
            errors = filter_validation(filter)
            if not errors:
                field = filter['field']
                condition = filter['condition']
                value = filter['value']
                if condition != 'contains':
                    ops = {
                        'eq': operator.eq,
                        'gt': operator.gt,
                        'lt': operator.lt
                    }
                    query = query.filter(ops[condition](getattr(Record, field), value))
                else:
                    query = query.filter(getattr(Record, field).like(f'%{value}%'))
            else:
                print(errors)
                res['errors'] = errors

        records_count = query.count()
        pages_count = (records_count // limit) + 1
        if sort == 'asc':
            query = query.order_by(order_by).offset(offset).limit(limit)
        else:
            query = query.order_by(desc(order_by)).offset(offset).limit(limit)
        records = query.all()

        res['pages_count'] = pages_count
        res['records'] = records

        return jsonify(res)
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create_record():
    input = request.get_json()
    errors = create_validation(input)
    if not errors:
        record = Record(
            title = input['title'],
            date = input['date'],
            amount = input['amount'],
            distance = input['distance']
        )

        db.session.add(record)
        db.session.commit()

        return '', 204
    return jsonify(errors)


if __name__ == '__main__':
    app.run()