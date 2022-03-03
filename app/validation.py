from datetime import datetime


def create_validation(data):
    title = data.get('title')
    date = data.get('date')
    amount = data.get('amount')
    distance = data.get('distance')
    errors = {
        'title': True,
        'date': True,
        'amount': True,
        'distance': True
    }
    
    if title and len(title) < 50:
        errors['title'] = False

    try:
        datetime.strptime(date, "%Y-%m-%d")
        errors['date'] = False
    except:
        pass
    
    try:
        if int(amount) >= 0:
            errors['amount'] = False
    except:
        pass

    try:
        if int(distance) >= 0:
            errors['distance'] = False
    except:
        pass

    if any(errors.values()):
        return errors
    else:
        return False


def filter_validation(data):
    value = data.get('value')
    field = data.get('field')
    condition = data.get('condition')
    errors = {
        'value': True,
        'field': True,
        'condition': True,
    }
    fields = ['title', 'amount', 'distance']
    conditions = ['contains', 'eq', 'gt', 'lt']

    if field and field in fields:
        errors['field'] = False

    if condition and condition in conditions:
        if field == 'title' and condition != 'contains':
            pass
        else:
            errors['condition'] = False

    if value and len(value) < 50:
        if condition != 'contains':
            try:
                int(value)
                errors['value'] = False
            except:
                pass
        else:
            errors['value'] = False
    
    if any(errors.values()):
        return errors
    else:
        return False

