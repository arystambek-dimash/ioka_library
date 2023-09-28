from ioka.exceptions import RequestError


def get_request_type(req_type):
    types = {
        'json': 'application/json; charset=utf-8'
    }
    return types.get(req_type, types['json'])


def check_data(data):
    for key, value in data.items():
        if value == '' or None:
            raise RequestError(key)
        if key == 'amount':
            try:
                int(value)
            except ValueError:
                raise ValueError('Amount must numeric')
