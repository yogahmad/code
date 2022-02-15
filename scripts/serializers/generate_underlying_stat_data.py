from django.forms import CharField
from rest_framework.serializers import IntegerField, Serializer, ListField, FloatField, DictField


class UnderlyingStatDataRequest(Serializer):
    a = DictField()
    h = DictField()
