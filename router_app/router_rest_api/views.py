from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.authentication import BasicAuthentication


# from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from router_api.models import Router
from .serializer import RouterSerializers
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.


class RouterView(APIView):
    def get_router_object(self, pk):
        try:
            return Router.objects.get(pk=pk)
        except Router.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        router_data = Router.objects.all()
        serializer = RouterSerializers(router_data, many=True)
        response = {}
        response["router_data"] = serializer.data
        return JsonResponse(response, status=status.HTTP_200_OK, safe=False)

    def post(self, request):
        serializer = RouterSerializers(data=request.data)
        response = {}
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            response["reason"] = data
            response["success"] = True
            return JsonResponse(response, status=status.HTTP_201_CREATED, safe=False)
        else:
            return JsonResponse(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
                safe=False
            )

    def put(self, request, format=None):
        data = request.data
        router_id = data["id"]
        router_obj = self.get_router_object(router_id)
        serializer = RouterSerializers(router_obj, data=request.data)
        response = {}
        if serializer.is_valid():
            serializer.save()
            response["reason"] = serializer.data
            response["success"] = True
            return JsonResponse(response, status=status.HTTP_200_OK)
        else:
            return JsonResponse(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        response = {}
        try:
            router_obj = self.get_router_object(pk=pk)
            router_obj.delete()
            response["success"] = True
            response["message"] = "Router data is deleted successfully"
            return JsonResponse(response, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            response["success"] = False
            response["message"] = "Router data is not deleted"
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
