from .bol_base_api import BolBaseAPI
from ...models import Shipment


class BolShipmentAPI(BolBaseAPI):

    def get_url(self) -> str:
        return super(BolShipmentAPI, self).get_url() + '/shipments/'

    def process_import(self, payload) -> list:
        shipment = self.make_api_call(
            self.get_url() + str(payload["id"]), {}, payload["token"])
        try:
            if shipment:
                Shipment.objects.create(
                    shipment_id=shipment["shipmentId"],
                    shop_client_id=payload["client_id"],
                    fulfilment_method=payload["fulfilment_method"],
                    shipment_date=shipment["shipmentDate"],
                    shipment_reference=shipment.get("shipmentReference"),
                    pick_up_point=shipment["pickUpPoint"],
                    zip_code=shipment["customerDetails"]["zipCode"],
                    country_code=shipment["customerDetails"]["countryCode"]
                )
        except Exception as e:
            print(e)
            pass

        return []
