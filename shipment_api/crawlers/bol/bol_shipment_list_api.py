from .bol_base_api import BolBaseAPI


class BolShipmentListAPI(BolBaseAPI):

    def get_url(self) -> str:
        return super(BolShipmentListAPI, self).get_url() + '/shipments'

    def process_import(self, payload) -> list:
        params = {"page": payload["page"],
                  "fulfilment-method": payload["fulfilment_method"]}
        response = self.make_api_call(self.get_url(), params, payload["token"])
        shipments = response.get("shipments") or []

        call_shipment = []
        for shipment in shipments:
            call_shipment.append({
                "class_name": "BolShipmentAPI",
                "payload": {
                    "token": payload["token"],
                    "id": shipment["shipmentId"],
                    "fulfilment_method": payload["fulfilment_method"],
                    "client_id": payload["client_id"]
                }
            })

        if len(shipments) == 50:
            # next page
            payload["page"] += 1
            call_shipment.append({
                "class_name": "BolShipmentListAPI",
                "payload": payload
            })

        return call_shipment
