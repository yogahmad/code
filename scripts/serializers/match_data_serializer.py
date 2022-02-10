from rest_framework.serializers import Serializer, IntegerField


class MatchDataSerializer(Serializer):
    id = IntegerField()
    team_a = IntegerField()
    team_h = IntegerField()
    event = IntegerField()
