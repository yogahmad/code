from rest_framework.serializers import (CharField, IntegerField, ListField,
                                        Serializer)


class PlayerDataSerializer(Serializer):
    id = IntegerField()
    first_name = CharField()
    second_name = CharField()
    web_name = CharField()
    now_cost = IntegerField()
    photo = CharField()
    chance_of_playing_this_round = IntegerField(allow_null=True)
    chance_of_playing_next_round = IntegerField(allow_null=True)
    team = IntegerField()
    element_type = IntegerField()


class PlayerDataRequest(Serializer):
    elements = ListField(child=PlayerDataSerializer())
