from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.job_categories.forms import UserForm
from apps.job_categories.models import User


class HomeListView(ListView):
    queryset = User.objects.all()
    template_name = 'apps/team_list/index.html'
    context_object_name = 'users'


class AddPersonView(CreateView):
    form_class = UserForm
    queryset = User.objects.all()
    success_url = reverse_lazy('home')
    template_name = 'apps/team_list/add.html'


class UpdatePersonView(UpdateView):
    queryset = User.objects.all()
    form_class = UserForm
    success_url = reverse_lazy('home')
    template_name = 'apps/team_list/edit.html'


class DeletePersonView(DeleteView):
    queryset = User.objects.all()
    success_url = reverse_lazy('home')
    template_name = 'apps/team_list/delete.html'
