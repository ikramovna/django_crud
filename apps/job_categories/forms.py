from django.forms import ModelForm

from apps.job_categories.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ()