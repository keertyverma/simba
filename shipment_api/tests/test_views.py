import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Shipment
from ..serializers import ShipmentSerializer


# initialize the APIClient app
client = Client()


class GetAllPuppiesTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        Shipment.objects.create(
            shipment_id=1234567,
            shop_client_id="abc-def-123",
            fulfilment_method='FBR',
            shipment_date='2020-02-07',
            shipment_reference="B2245O",
            pick_up_point=True,
            zip_code="560000",
            country_code="NA"
        )

        # Puppy.objects.create(
        #     name='Muffin', age=1, breed='Gradane', color='Brown')
        # Puppy.objects.create(
        #     name='Rambo', age=2, breed='Labrador', color='Black')
        # Puppy.objects.create(
        #     name='Ricky', age=6, breed='Labrador', color='Brown')

    def test_get_all_shipment(self):
        # get API response

        headers = {
            'Authorization': 'Token c627fc714da5a0d06c8b8bbb5ae6060cc653b78c'
        }
        response = client.get(reverse('get-all-shipments'), headers=headers)
        # get data from db
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
