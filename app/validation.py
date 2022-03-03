from datetime import datetime


def validation_errors(data):
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

