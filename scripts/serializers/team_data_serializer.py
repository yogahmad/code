from rest_framework.serializers import Serializer, IntegerField, CharField, ListField


class TeamDataSerializer(Serializer):
    id = IntegerField()
    name = CharField()
    short_name = CharField()
    strength_attack_home = IntegerField()
    strength_attack_away = IntegerField()
    strength_defence_home = IntegerField()
    strength_defence_away = IntegerField()


class TeamDataRequest(Serializer):
    teams = ListField(child=TeamDataSerializer())
