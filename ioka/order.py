from ioka import api as ioka_api
from ioka import helpers as helper
from ioka import utils


class Order:
    def __init__(self, api: ioka_api.Api):
        self._api = api

    def create_order(self, data: dict):
        path = "v2/orders/"
        params = {
            "amount": data.get("amount"),
            "currency": data.get("currency"),
        }
        helper.check_data(params)
        params.update(data)
        result = self._api.post(path, data=params)
        return utils.from_json(utils.to_json(result)).get('response', '')

    def get_orders(self):
        path = "v2/orders/"
        result = self._api.post(path, data={})
        return utils.from_json(utils.to_json(result)).get('response', '')

    def get_order_by_id(self, order_id):
        path = f"v2/orders/{order_id}"
        result = self._api.post(path, data={})
        return utils.from_json(utils.to_json(result)).get('response', '')

    def cancel_order(self, data, order_id):
        path = f"v2/orders/{order_id}/cancel"
        params = {
            'order_id': data.get("reason")
        }
        helper.check_data(params)
        params.update(data)
        result = self._api.post(path, data=data)
        return utils.from_json(utils.to_json(result)).get('response', '')
