from django.forms import ModelForm

from apps.card_location.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ()