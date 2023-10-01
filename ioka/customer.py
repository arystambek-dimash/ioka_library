from ioka import api as ioka_api
from ioka import utils
from ioka import helpers as helper


class Customer:
    def __init__(self, api: ioka_api.Api = None):
        self._api = api
        self.__headers__ = self._api._headers()

    def get_customers(self):
        path = "/v2/customers"
        result = self._api.post(path, data={}, headers=self.__headers__)
        return utils.from_json(utils.to_json(result)).get('response', '')

    def create_customers(self, data: dict):
        path = "/v2/customers"
        params = {
            "external_id": data.get("external_id"),
            "email": data.get("email"),
            "phone": data.get("phone"),
            "fingerprint": data.get("fingerprint"),
            "phone_check_date": data.get("phone_check_date"),
            "channel": data.get("channel")
        }
        helper.check_data(params)
        params.update(data)
        result = self._api.post(path, data=params, headers=self.__headers__)
        return utils.from_json(utils.to_json(result)).get('response', '')

    def get_customer_by_id(self, customer_id: int):
        path = f"v2/customers/{customer_id}"
        result = self._api.post(path, data={}, headers=self.__headers__)
        return utils.from_json(utils.to_json(result)).get('response', '')

    def get_events(self, customer_id: int):
        path = f"v2/customers/{customer_id}/events"
        result = self._api.post(path, data={}, headers=self.__headers__)
        return utils.from_json(utils.to_json(result)).get('response', '')

    def delete_customer(self, customer_id: int, data: dict):
        path = f"v2/customers/{customer_id}"
        params = {
            "code": data.get("code"),
            "message": data.get("message")
        }
        helper.check_data(params)
        result = self._api.post(path, data=params, headers=self.__headers__)
        return utils.from_json(utils.to_json(result)).get('response', '')
