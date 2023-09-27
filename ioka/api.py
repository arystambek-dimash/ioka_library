import json

from helpers import get_request_type
from ioka import exceptions

import os
import requests
import ioka.utils as utils


class Api:
    def __init__(self, **kwargs):
        self.secret_key = kwargs.get("secret_key", '')
        self.request_type = kwargs.get('request_type') or get_request_type('json')
        if not self.secret_key:
            self.secret_key = os.environ.get('IOKA_SECRETKEY', '')
            if not self.secret_key:
                raise ValueError("API key not found")
        self.api_url = "https://stage-api.ioka.kz/v2/"

    def _headers(self):
        return {
            'API-KEY': self.secret_key,
            'Content-Type': get_request_type(self.request_type),
        }

    def _request(self, url, method, data, headers):
        response = requests.request(method, url, data=data, headers=headers)
        return self._response(response, response.content.decode('utf-8'))

    def _response(self, response, content):
        status = response.status_code
        if status in (200, 201):
            return content

        raise exceptions.ServiceError(
            'Response code is: {status}'.format(status=status))

    def post(self, url, data, headers=None):
        if headers is None:
            headers = {}

        data_v2 = {
            "data": utils.encode_to_64(data)
        }
        data_string = utils.to_json(data_v2)
        return self._request(url, 'POST', data=data_string,
                             headers=utils.merge_dict(headers, self._headers()))


api = Api(secret_key="sqafdsafsdf")
payload = json.dumps({
    'amount': 10000
})
api.post("https://stage-api.ioka.kz/v2/orders", data=payload)
