from ioka.helpers import get_request_type
from ioka import exceptions

import os
import requests
import ioka.utils as utils


class Api:
    API_URL = "https://api.ioka.kz"

    def __init__(self, api_key=None, is_test=False, request_type=None):
        """
        Initializes the API class with the given parameters.

        :param api_key: API key for accessing the endpoint.
                        If not provided, it tries to get it from an environment variable.
        :param request_type: Type of the request. If not provided, defaults using get_request_type.
        """
        self.api_key = api_key or os.environ.get('IOKA_SECRETKEY')
        if is_test:
            self.API_URL = "https://stage-api.ioka.kz"
        if not self.api_key:
            raise ValueError("API key not found")

        self.request_type = request_type or get_request_type('json')
        self.api_url = self.API_URL

    def _headers(self):
        return {
            'API-KEY': self.api_key,
            'Content-Type': get_request_type(self.request_type),
        }

    def _request(self, url, method, data, headers):
        response = requests.request(method, url, data=data, headers=headers)
        return self._response(response, response.content.decode('utf-8'))

    @staticmethod
    def _response(response, content):
        status = response.status_code
        if status in (200, 201):
            return content
        elif status == 401:
            raise exceptions.Unauthorized(f'Response code is: {status}'.format(status=status))
        raise exceptions.ServiceError(
            'Response code is: {status}'.format(status=status))

    def post(self, url, data, headers=None):
        if headers is None:
            headers = {}

        data_v2 = {
            "data": utils.encode_to_64(data)
        }
        data_string = utils.to_json(data_v2)
        endpoint_url = utils.join_url(self.api_url, url)
        return self._request(endpoint_url, 'POST', data=data_string,
                             headers=utils.merge_dict(headers, self._headers()))
