from django.db import models
from django.utils.translation import gettext_lazy as _

TRIGGER_TYPE_CHOICES = ((0, "entered"), (1, "exited"))


class Gps(models.Model):
    objects = models.QuerySet

    id = models.BigAutoField(primary_key=True, editable=False)
    occurred_at = models.DateTimeField(_("occurred at"), blank=True, null=True)
    location_map_image_url = models.CharField(
        _("location map image url"), max_length=1024, blank=True, null=True
    )
    location_map_url = models.CharField(
        _("location map url"), max_length=1024, blank=True, null=True
    )
    trigger_type = models.IntegerField(
        _("trigger type"), blank=False, null=False, choices=TRIGGER_TYPE_CHOICES
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return "{}_{}".format(
            self.get_trigger_type_display(), self.occurred_at.isoformat()
        )

    class Meta:
        verbose_name = "Gps"
        verbose_name_plural = "Gps"
