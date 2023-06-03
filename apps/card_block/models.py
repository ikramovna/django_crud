from django.db import models


class User(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    shot1 = models.IntegerField()
    shot2 = models.IntegerField()
    shot3 = models.IntegerField()
    image = models.ImageField(upload_to='users/', null=True, blank=True)