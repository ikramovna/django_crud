from django.forms import ModelForm

from apps.simple_job.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ()
