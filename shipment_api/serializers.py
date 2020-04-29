from rest_framework import serializers
from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'


class ShipmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ('shipment_date', 'shipment_reference',
                  'pick_up_point', 'billing_details_first_name', 'billing_details_surname')
