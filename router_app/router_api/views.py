from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializer import RouterSerializers
from .models import Router
from .pagination import StandardResultsSetPagination


def RouterList(request):
    return render(request, "router.html", {})


class RouterListing(ListAPIView):
    # set the pagination and serializer class
    pagination_class = StandardResultsSetPagination
    serializer_class = RouterSerializers

    def get_queryset(self):
        # filter the queryset based on the filters applied

        queryList = Router.objects.all()
        sapid = self.request.query_params.get('sapid', None)
        # variety = self.request.query_params.get('variety', None)
        # province = self.request.query_params.get('province', None)
        # region = self.request.query_params.get('region', None)
        # sort_by = self.request.query_params.get('sort_by', None)

        if sapid:
            queryList = queryList.filter(sapid=sapid)

        # sort it if applied on based on price/points

        # if sort_by == "price":
        #     queryList = queryList.order_by("price")
        # elif sort_by == "points":
        # #     queryList = queryList.order_by("points")
        return queryList


def getSapids(request):

    if request.method == "GET" and request.is_ajax():
        sapids = Router.objects.exclude(sapid__isnull=True).\
            exclude(sapid__exact='').order_by('sapid').values_list('sapid').distinct()
        sapids = [i[0] for i in list(sapids)]
        data = {
            "sapids": sapids,
        }
        return JsonResponse(data, status=200)


# def getvariety(request):
#     if request.method == "GET" and request.is_ajax():
#         # get all the varities from the database excluding
#         # null and blank values

#         variety = Wine.objects.exclude(variety__isnull=True).\
#         	exclude(variety__exact='').order_by('variety').values_list('variety').distinct()
#         variety = [i[0] for i in list(variety)]
#         data = {
#             "variety": variety,
#         }
#         return JsonResponse(data, status = 200)


# def getProvince(request):
#     # get the provinces for given country from the
#     # database excluding null and blank values

#     if request.method == "GET" and request.is_ajax():
#         country = request.GET.get('country')
#         province = Wine.objects.filter(country = country).\
#             	exclude(province__isnull=True).exclude(province__exact='').\
#             	order_by('province').values_list('province').distinct()
#         province = [i[0] for i in list(province)]
#         data = {
#             "province": province,
#         }
#         return JsonResponse(data, status = 200)


# def getRegion(request):
#     # get the regions for given province from the
#     # database excluding null and blank values

#     if request.method == "GET" and request.is_ajax():
#         province = request.GET.get('province')
#         region = Wine.objects.filter(province = province).\
#                 exclude(region__isnull=True).exclude(region__exact='').values_list('region').distinct()
#         region = [i[0] for i in list(region)]
#         data = {
#             "region": region,
#         }
#         return JsonResponse(data, status = 200)
