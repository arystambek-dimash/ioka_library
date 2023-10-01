import unittest
from unittest.mock import MagicMock, patch
from ioka.api import Api
from ioka import utils


class TestApi(unittest.TestCase):

    def test_post(self):
        api = Api(api_key='your_api_key')
        url = 'v2/orders'
        data = {'amount': 500000}
        expected_response = 'Mocked Response'

        with patch('ioka.api.requests.request') as mock_request:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.content.decode.return_value = expected_response
            mock_request.return_value = mock_response

            response = api.post(url, data)
            mock_request.assert_called_once_with(
                'POST',
                f'https://api.ioka.kz/{url}',
                data=f'{{"data":{utils.encode_to_64(data)}}}',
                headers={'API-KEY': 'your_api_key', 'Content-Type': 'application/json; charset=utf-8'},
            )
            self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
