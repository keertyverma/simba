from django.test import TestCase
from ..models import Shipment


class ShipmentTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Shipment.objects.create(
            shipment_id=1234567, shop_client_id="abc-def-123", fulfilment_method='FBR', shipment_date='2020-02-07')
        Shipment.objects.create(
            shipment_id=1234789, shop_client_id="abc-iok-123", fulfilment_method='FBB', shipment_date='2020-02-08')

    # def test_shipment_details(self):
    #     shipment_a = Shipment.objects.get(shipment_id=1234567)
    #     shipment_b = Shipment.objects.get(shipment_id=1234789)
    #     self.assertEqual(
    #         shipment_a.get_shipment_details(), "Shipment ID =  1234567 and shipment data =  2020-02-07")
    #     self.assertEqual(
    #         shipment_a.get_shipment_details(), "Shipment ID =  1234789 and shipment data =  2020-02-08")
