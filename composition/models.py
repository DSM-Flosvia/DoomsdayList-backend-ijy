from django.utils import timezone
from django.db import models


class Memo(models.model):
    text = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
