from django.contrib import admin

from .models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "status",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)
    fields = ("status",)


admin.site.register(Status, StatusAdmin)
