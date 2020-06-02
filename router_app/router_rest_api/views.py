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


class RouterDetail(APIView):

    def get_router_object(self, pk):
        try:
            return Router.objects.get(pk=pk)
        except Router.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RouterSerializers(snippet)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        router = self.get_router_object(pk)
        serializer = RouterSerializers(router, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        router = self.get_router_object(pk)
        router.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
