from .models import Shipment
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response


class ShipmentListView(generics.ListAPIView):
    queryset = Shipment.objects.all()
    serializer_class = serializers.ShipmentSerializer


class ShipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipment.objects.all()
    serializer_class = serializers.ShipmentDetailSerializer

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
