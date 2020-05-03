"""
Class used to crawl all shipment data from bol.com.
* Setting url to get all shipment API
* Getting shipments data from all pages
* Creating list with shipment data to pass it as celery task

"""
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
            if payload['last_updated_at'] >= shipment['shipmentDate']:
                break

            call_shipment.append({
                "class_name": "BolShipmentAPI",
                "payload": {
                    "token": payload["token"],
                    "id": shipment["shipmentId"],
                    "fulfilment_method": payload["fulfilment_method"],
                    "client_id": payload["client_id"]
                }
            })

        if len(call_shipment) == 50:
            # next page
            payload["page"] += 1
            call_shipment.append({
                "class_name": "BolShipmentListAPI",
                "payload": payload
            })

        return call_shipment
