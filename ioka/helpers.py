def get_request_type(req_type):
    types = {
        'json': 'application/json; charset=utf-8'
    }
    return types.get(req_type, types['json'])
