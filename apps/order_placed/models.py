from django.db.models import Model, CharField, ImageField


class User(Model):
    description = CharField(max_length=255)
    price = CharField(max_length=255)
    discount = CharField(max_length=255)
    image = ImageField(upload_to='users/', null=True, blank=True)