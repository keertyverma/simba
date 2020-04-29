from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Shipment, Seller


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'


class ShipmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ('shipment_date', 'shipment_reference',
                  'pick_up_point', 'billing_details_first_name', 'billing_details_surname')


class SellerRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    shop_name = serializers.CharField()
    bol_client_id = serializers.CharField()
    bol_client_secret = serializers.CharField()

    def get_cleaned_data(self):
        super(SellerRegisterSerializer, self).get_cleaned_data()

        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'shop_name': self.validated_data.get('shop_name', ''),
            'bol_client_id': self.validated_data.get('bol_client_id', ''),
            'bol_client_secret': self.validated_data.get('bol_client_secret', '')
        }
