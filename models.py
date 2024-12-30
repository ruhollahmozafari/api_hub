from django.conf import settings
from django.db import models

class ServiceAPILog(models.Model):
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True, )
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    endpoint = models.CharField(max_length=5000)
    service_name = models.CharField(max_length=100, null=True, blank=True, )
    request_data = models.JSONField(null=True, blank=True)
    response_data = models.JSONField(null=True, blank=True)
    status_code = models.SmallIntegerField(null=True, blank=True, )
    ok = models.BooleanField(default=True, blank=True,null=True)

    class Meta:
        abstract = getattr(settings, "SAVE_API_HUB_TO_DB", False) #TODO: api hub
        ordering = ("-pk",)


