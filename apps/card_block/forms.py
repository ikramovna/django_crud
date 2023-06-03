from django.forms import ModelForm

from apps.card_block.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ()
