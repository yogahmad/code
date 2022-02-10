from rest_framework.serializers import IntegerField, Serializer


class MatchDataSerializer(Serializer):
    id = IntegerField()
    team_a = IntegerField()
    team_h = IntegerField()
    event = IntegerField(allow_null=True)
