from django.contrib import admin

from stats.models import UnderlyingStat


@admin.register(UnderlyingStat)
class UnderlyingStatAdmin(admin.ModelAdmin):
    pass
