import unittest
from unittest.mock import MagicMock

from ioka.payment import Payment


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.mock_api = MagicMock()
        self.payment = Payment(self.mock_api)

    def test_get_payments(self):
        order_id = 123
        expected_response = {'response': 'list_of_payments'}
        self.mock_api.post.return_value = expected_response
        result = self.payment.get_payments(order_id)
        self.assertEqual(result, 'list_of_payments')
        self.mock_api.post.assert_called_once_with(f'/v2/orders/{order_id}/payments', data={})

    def test_create_payment(self):
        order_id = 123
        data = {
            'pan': '5555555555555599',
            'exp': '1224',
            'cvc': '123',
            'holder': 'John Doe',
            'save': True,
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'card_id': 'card_12345',
            'fingerprint': 'abcd1234',
            'phone_check_date': '2023-10-01',
            'channel': 'web'
        }
        expected_response = {'response': 'created_payment'}
        self.mock_api.post.return_value = expected_response
        result = self.payment.create_payment(order_id, data)
        self.assertEqual(result, 'created_payment')
        self.mock_api.post.assert_called_once_with(f'/v2/orders/{order_id}/payments/card', data=data)

    def test_create_tool_payment(self):
        order_id = 123
        data = {
            'pan': '5555555555555599',
            'exp': '1224',
            'cvc': '123',
            'holder': 'John Doe',
            'save': True,
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'card_id': 'card_12345',
            'fingerprint': 'abcd1234',
            'phone_check_date': '2023-10-01',
            'channel': 'web'
        }
        expected_response = {'response': 'created_tool_payment'}
        self.mock_api.post.return_value = expected_response
        result = self.payment.create_tool_payment(order_id, data)
        self.assertEqual(result, 'created_tool_payment')
        self.mock_api.post.assert_called_once_with(f'/v2/orders/{order_id}/payments/card', data=data)


if __name__ == '__main__':
    unittest.main()
