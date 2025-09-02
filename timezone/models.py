from django.db import models
from django.conf import settings

class TimezoneEntry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='timezones'
    )
    name = models.CharField(max_length=100)  # Friendly name
    city = models.CharField(max_length=100)  # City name
    gmt_offset = models.IntegerField(help_text="Offset to GMT in hours")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.city})"
