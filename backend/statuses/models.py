from django.db import models
from django.utils.translation import gettext_lazy as _

STATUS_CHOICES = ((0, "inactive"), (1, "active"))


class Status(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    status = models.IntegerField(
        _("status"), blank=False, null=False, choices=STATUS_CHOICES
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return "{}_{}".format(self.get_status_display(), self.created_at.isoformat())

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"
