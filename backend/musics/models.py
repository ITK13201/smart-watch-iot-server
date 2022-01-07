from django.db import models
from django.utils.translation import gettext_lazy as _


class Music(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    file_path = models.CharField(
        _("file path"), max_length=512, blank=False, null=False
    )
    url = models.CharField(_("url"), max_length=512, blank=False, null=False)
    bpm = models.FloatField(_("bpm"), blank=False, null=False)
    length = models.FloatField(_("length [sec]"), default=0.0, blank=False, null=False)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.file_path

    class Meta:
        verbose_name = "Music"
        verbose_name_plural = "Musics"
