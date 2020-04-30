from .models import Shipment
from . import serializers
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


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


class ShipmentRefreshView(generics.CreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = serializers.ShipmentSerializer

    def create(self, request, *args, **kwargs):
        super(ShipmentRefreshView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)
