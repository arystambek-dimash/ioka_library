import unittest
from unittest.mock import MagicMock

from ioka.customer import Customer


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.mock_api = MagicMock()
        self.customer = Customer(api=self.mock_api)

    def test_get_customers(self):
        expected_response = {'response': 'list_of_customers'}
        self.mock_api.post.return_value = expected_response
        result = self.customer.get_customers()
        self.assertEqual(result, 'list_of_customers')
        self.mock_api.post.assert_called_once_with('/v2/customers', data={}, headers=self.customer.__headers__)

    def test_create_customers(self):
        data = {
            'external_id': 123,
            'email': 'test@example.com',
            'phone': '1234567890',
            'fingerprint': 'abcd1234',
            'phone_check_date': '2023-10-01',
            'channel': 'web'
        }
        expected_response = {'response': 'created_customer'}
        self.mock_api.post.return_value = expected_response
        result = self.customer.create_customers(data)
        self.assertEqual(result, 'created_customer')
        self.mock_api.post.assert_called_once_with('/v2/customers', data=data,
                                                   headers=self.customer.__headers__)

    def test_get_customer_by_id(self):
        customer_id = 123
        expected_response = {'response': 'customer_details'}
        self.mock_api.post.return_value = expected_response
        result = self.customer.get_customer_by_id(customer_id)
        self.assertEqual(result, 'customer_details')
        self.mock_api.post.assert_called_once_with(f'v2/customers/{customer_id}', data={},
                                                   headers=self.customer.__headers__)

    def test_get_events(self):
        customer_id = 123
        expected_response = {'response': 'list_of_events'}
        self.mock_api.post.return_value = expected_response
        result = self.customer.get_events(customer_id)
        self.assertEqual(result, 'list_of_events')
        self.mock_api.post.assert_called_once_with(f'v2/customers/{customer_id}/events', data={},
                                                   headers=self.customer.__headers__)

    def test_delete_customer(self):
        customer_id = 123
        data = {'code': '123', 'message': 'Test message'}
        expected_response = {'response': 'deleted_customer'}
        self.mock_api.post.return_value = expected_response
        result = self.customer.delete_customer(customer_id, data)
        self.assertEqual(result, 'deleted_customer')
        self.mock_api.post.assert_called_once_with(f'v2/customers/{customer_id}', data=data,
                                                   headers=self.customer.__headers__)


if __name__ == '__main__':
    unittest.main()
