from rest_framework.serializers import IntegerField, ListField, Serializer


class PlayersPointDataSerializer(Serializer):
    minutes = IntegerField()
    goals_scored = IntegerField()
    assists = IntegerField()
    clean_sheets = IntegerField()
    goals_conceded = IntegerField()
    own_goals = IntegerField()
    penalties_saved = IntegerField()
    penalties_missed = IntegerField()
    yellow_cards = IntegerField()
    red_cards = IntegerField()
    saves = IntegerField()
    bonus = IntegerField()
    selected = IntegerField()
    fixture = IntegerField()


class PlayersPointDataRequest(Serializer):
    history = ListField(child=PlayersPointDataSerializer())
