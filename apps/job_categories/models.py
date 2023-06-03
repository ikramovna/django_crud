from django.db import models


class User(models.Model):
    job = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='users/', null=True, blank=True)