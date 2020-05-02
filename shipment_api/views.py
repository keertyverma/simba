from django.contrib.auth import get_user_model
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import Shipment
from .tasks import trigger_shipment_import


class ShipmentListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Shipment.objects.all()
    serializer_class = serializers.ShipmentSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Shipment.objects.filter(shop_client_id=user.bol_client_id)


class ShipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipment.objects.all()
    serializer_class = serializers.ShipmentDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Shipment.objects.filter(shop_client_id=user.bol_client_id)

    def retrieve(self, request, *args, **kwargs):
        super(ShipmentDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)


class ShipmentDataRefreshView(generics.CreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = serializers.ShipmentDataRefreshSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # call import_data celery task
        trigger_shipment_import.delay("bol",
                                      {"client_id": request.user.bol_client_id, "client_secret": request.user.bol_client_secret})

        request.data['shop_client_id'] = request.user.bol_client_id
        request.data['username'] = request.user.username

        super(ShipmentDataRefreshView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully refreshed shipment data",
                    "result": request.data}
        return Response(response)


class SellerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Reads, deletes and updates UserModel fields
    Accepts GET, PUT, PATCH, DELETE methods.
    Default accepted fields: username, first_name, last_name
    Default display fields: pk, username, email, first_name, last_name
    Read-only fields: pk, email
    Returns UserModel fields.
    """
    serializer_class = serializers.SellerDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        """
        Adding this method since it is sometimes called when using
        django-rest-swagger
        https://github.com/Tivix/django-rest-auth/issues/275
        """
        return get_user_model().objects.none()
