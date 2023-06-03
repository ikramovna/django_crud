from django.forms import ModelForm

from apps.news.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ()
