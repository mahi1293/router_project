from django.urls import path
from router_api import views

urlpatterns = [
    path('', views.RouterList),
    path("router_listing/", views.RouterListing.as_view(), name='listing'),
    path("ajax/sapids/", views.getSapids, name='get_sapids'),
]
