from django.forms import ModelForm

from apps.order_placed.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ()
