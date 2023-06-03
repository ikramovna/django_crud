from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.simple_job.forms import UserForm
from apps.simple_job.models import User


class HomeListView(ListView):
    queryset = User.objects.all()
    template_name = 'apps/simple_job/index.html'
    context_object_name = 'users'
    paginate_by = 10


class AddPersonView(CreateView):
    form_class = UserForm
    queryset = User.objects.all()
    success_url = reverse_lazy('home')
    template_name = 'apps/simple_job/add.html'


class UpdatePersonView(UpdateView):
    queryset = User.objects.all()
    form_class = UserForm
    success_url = reverse_lazy('home')
    template_name = 'apps/simple_job/edit.html'


class DeletePersonView(DeleteView):
    queryset = User.objects.all()
    success_url = reverse_lazy('home')
    template_name = 'apps/simple_job/delete.html'
