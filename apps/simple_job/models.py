from django.db import models


class User(models.Model):
    job = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)