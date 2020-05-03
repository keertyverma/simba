from django.urls import path
from . import views

urlpatterns = [
    path('shipment/', views.ShipmentListView.as_view(), name="get-all-shipments"),
    path('shipment/<int:pk>/', views.ShipmentDetailView.as_view(), name=None),
    path('shipment/refresh/', views.ShipmentDataRefreshView.as_view(), name=None),
    path('seller/', views.SellerDetailsView.as_view(), name=None)
]
