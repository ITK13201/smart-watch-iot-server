from django.contrib import admin

from .models import Gps


class GpsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "occurred_at",
        "location_map_image_url",
        "location_map_url",
        "trigger_type",
        "created_at",
        "updated_at"
    )
    ordering = ("-occurred_at",)
    fields = (
        "occurred_at",
        "location_map_image_url",
        "location_map_url",
        "trigger_type"
    )

admin.site.register(Gps, GpsAdmin)
