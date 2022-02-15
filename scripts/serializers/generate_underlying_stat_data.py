from django.forms import CharField
from rest_framework.serializers import (DictField, FloatField, IntegerField,
                                        ListField, Serializer)


class UnderlyingStatDataRequest(Serializer):
    a = DictField()
    h = DictField()
