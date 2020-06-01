from rest_framework import serializers
from router_api.models import Router


class RouterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = "__all__"
