from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name=None),
    path('create', views.UserCreateView.as_view(), name=None),
    path('<int:pk>', views.UserDetailView.as_view(), name=None)
]
