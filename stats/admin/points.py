from django.contrib import admin

from stats.models.points import Point


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    pass
