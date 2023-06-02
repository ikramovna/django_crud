from django.forms import ModelForm

from apps.news_wdj.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ()
