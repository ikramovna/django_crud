from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    image = models.ImageField(upload_to='users/', null=True, blank=True)