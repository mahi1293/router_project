from django.urls import path
from router_rest_api import views

urlpatterns = [
    path("api/", views.RouterView.as_view(), name='api_view'),
]
