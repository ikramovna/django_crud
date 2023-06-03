from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.order_placed.forms import UserForm
from apps.order_placed.models import User


class HomeListView(ListView):
    queryset = User.objects.all()
    template_name = 'apps/index.html'
    context_object_name = 'users'


class AddPersonView(CreateView):
    form_class = UserForm
    queryset = User.objects.all()
    success_url = reverse_lazy('home')
    template_name = 'apps/add.html'


class UpdatePersonView(UpdateView):
    queryset = User.objects.all()
    form_class = UserForm
    success_url = reverse_lazy('home')
    template_name = 'apps/edit.html'


class DeletePersonView(DeleteView):
    queryset = User.objects.all()
    success_url = reverse_lazy('home')
    template_name = 'apps/delete.html'