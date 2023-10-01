import unittest
from unittest.mock import MagicMock

from ioka.order import Order


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.mock_api = MagicMock()
        self.order = Order(self.mock_api)

    def test_create_order(self):
        data = {
            'amount': 100,
            'currency': 'USD',
        }
        expected_response = {'response': 'created_order'}
        self.mock_api.post.return_value = expected_response
        result = self.order.create_order(data)
        self.assertEqual(result, 'created_order')
        self.mock_api.post.assert_called_once_with('v2/orders/', data=data)

    def test_get_orders(self):
        expected_response = {'response': 'list_of_orders'}
        self.mock_api.post.return_value = expected_response
        result = self.order.get_orders()
        self.assertEqual(result, 'list_of_orders')
        self.mock_api.post.assert_called_once_with('v2/orders/', data={})

    def test_get_order_by_id(self):
        order_id = 123
        expected_response = {'response': 'order_details'}
        self.mock_api.post.return_value = expected_response
        result = self.order.get_order_by_id(order_id)
        self.assertEqual(result, 'order_details')
        self.mock_api.post.assert_called_once_with(f'v2/orders/{order_id}', data={})

    def test_cancel_order(self):
        order_id = 123
        data = {'reason': 'Cancelled by user'}
        expected_response = {'response': 'order_cancelled'}
        self.mock_api.post.return_value = expected_response
        result = self.order.cancel_order(data, order_id)
        self.assertEqual(result, 'order_cancelled')
        self.mock_api.post.assert_called_once_with(f'v2/orders/{order_id}/cancel', data=data)


if __name__ == '__main__':
    unittest.main()
