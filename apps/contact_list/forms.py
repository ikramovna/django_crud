from django.forms import ModelForm

from apps.contact_list.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ()
