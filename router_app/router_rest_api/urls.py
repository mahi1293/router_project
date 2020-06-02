from django.urls import path
from router_rest_api import views

urlpatterns = [
    path("routers/", views.RouterView.as_view(), name='api_view'),
    path("router/(?P<pk>[0-9]+)/", views.RouterDetail.as_view(), name='api_detail'),

]
