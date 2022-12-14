from django.db import models
from api.models import Group

class Calendar(models.Model):
    values = models.JSONField(blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)