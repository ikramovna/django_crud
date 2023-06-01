from django.db import models
from django.db.models import Model, TextChoices


class User(Model):
    class StatusChoice(TextChoices):
        FULL_TIME = 'full_time', 'Full_time'
        REMOTE = 'remote', 'Remote'
        CONTRACT = 'contract', 'Contract'
        WFH = 'wfh', 'Wfh'

    job = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    location = models.CharField(max_length=255)