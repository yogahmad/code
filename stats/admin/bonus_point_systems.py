from django.contrib import admin

from stats.models.bonus_point_systems import BonusPointSystem


@admin.register(BonusPointSystem)
class BonusPointSystemAdmin(admin.ModelAdmin):
    pass
