from django.urls import path
from . import views

urlpatterns = [
    path('shipment/', views.ShipmentListView.as_view(), name=None),
    path('shipment/<int:pk>', views.ShipmentDetailView.as_view(), name=None),
    path('shipment/refresh', views.ShipmentRefreshView.as_view(), name=None),
    path('account/user/', views.SellerDetailsView.as_view(), name=None)
]
