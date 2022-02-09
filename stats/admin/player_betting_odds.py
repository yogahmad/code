from django.contrib import admin

from stats.models.player_betting_odds import PlayerBettingOdd


@admin.register(PlayerBettingOdd)
class PlayerBettingOddAdmin(admin.ModelAdmin):
    pass
