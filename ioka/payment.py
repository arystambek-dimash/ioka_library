from ioka import api as ioka_api
from ioka import helpers as helper
from ioka import utils


class Payment:
    def __init__(self, api: ioka_api.Api):
        self._api = api

    def get_payments(self, order_id: int):
        path = f"/v2/orders/{order_id}/payments"
        result = self._api.post(path, data={})
        return utils.from_json(utils.to_json(result)).get('response', '')

    def create_payment(self, order_id: int, data: dict):
        path = f"/v2/orders/{order_id}/payments/card"
        params = {
            "pan": data.get("pan"),
            "exp": data.get("exp"),
            "cvc": data.get("cvc"),
            "holder": data.get("holder"),
            "save": data.get("save"),
            "email": data.get("email"),
            "phone": data.get("phone"),
            "card_id": data.get("card_id") or None,
            "fingerprint": data.get("fingerprint"),
            "phone_check_date": data.get("phone_check_date"),
            "channel": data.get("channel")
        }
        helper.check_data(params)
        params.update(data)
        result = self._api.post(path, data=params)
        return utils.from_json(utils.to_json(result)).get('response', '')

    def create_tool_payment(self,order_id:int,data:dict):
        path = f"/v2/orders/{order_id}/payments/card"
        params = {
            "pan": data.get("pan"),
            "exp": data.get("exp"),
            "cvc": data.get("cvc"),
            "holder": data.get("holder"),
            "save": data.get("save"),
            "email": data.get("email"),
            "phone": data.get("phone"),
            "card_id": data.get("card_id") or None,
            "fingerprint": data.get("fingerprint"),
            "phone_check_date": data.get("phone_check_date"),
            "channel": data.get("channel")
        }
        helper.check_data(params)
        params.update(data)
        result = self._api.post(path, data=params)
        return utils.from_json(utils.to_json(result)).get('response', '')
