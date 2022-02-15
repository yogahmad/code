from rest_framework.serializers import DictField, Serializer


class UnderlyingStatDataRequest(Serializer):
    a = DictField()
    h = DictField()
