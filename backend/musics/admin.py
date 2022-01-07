from django.contrib import admin

from .models import Music


class MusicAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "file_path",
        "url",
        "bpm",
        "length",
        "created_at",
        "updated_at",
    )
    ordering = ("file_path",)
    fields = ("file_path", "url", "bpm", "length")


admin.site.register(Music, MusicAdmin)
