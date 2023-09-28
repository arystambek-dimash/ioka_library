import json
import re
import jwt


def encode_to_64(data):
    return jwt.encode({"data": data}, "ioka", algorithm="HS256")


def decode_to_str(data_jwt):
    return jwt.decode(data_jwt, "ioka", algorithms=["HS256"])


def to_json(data):
    return json.dumps(data)


def from_json(json_string):
    return json.loads(json_string)


def join_url(url, *paths):
    for path in paths:
        url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url


def merge_dict(x, y):
    z = x.copy()
    z.update(y)
    return z
