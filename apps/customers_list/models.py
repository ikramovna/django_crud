from django.db.models import Model, CharField, ImageField


class User(Model):
    name = CharField(max_length=255)
    city = CharField(max_length=255)
    salary = CharField(max_length=255)
    image = ImageField(upload_to='users/', null=True, blank=True)