from django.forms import ModelForm

from apps.team_list.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ()
