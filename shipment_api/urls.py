from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ShipmentListView.as_view(), name=None),
    path('', views.ShipmentListView.as_view({"get": "list"}), name=None),
    path('<int:pk>', views.ShipmentDetailView.as_view(), name=None),
    path('refresh', views.ShipmentRefreshView.as_view(), name=None)
]
