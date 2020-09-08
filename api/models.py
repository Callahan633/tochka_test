import uuid

from django.db import models


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    credentials = models.CharField(max_length=255, null=False, blank=False)
    current_balance = models.DecimalField(max_digits=20, decimal_places=2, blank=False)
    reserved_operations = models.DecimalField(max_digits=20, decimal_places=2, blank=False)
    is_opened = models.BooleanField(default=True)
