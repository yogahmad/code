from django.contrib import admin

from kits.models import Kit


@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    pass
