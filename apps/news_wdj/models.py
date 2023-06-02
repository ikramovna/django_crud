from django.db import models


class User(models.Model):
    new = models.CharField(max_length=255)
    date = models.DateField(max_length=255)
    image = models.ImageField(upload_to='user/', null=True, blank=True)