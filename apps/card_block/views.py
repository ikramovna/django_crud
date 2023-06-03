from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.card_block.forms import UserForm
from apps.card_block.models import User


class HomeListView(ListView):
    queryset = User.objects.all()
    template_name = 'apps/card_block/index.html'
    context_object_name = 'users'


class AddPersonView(CreateView):
    form_class = UserForm
    queryset = User.objects.all()
    success_url = reverse_lazy('home')
    template_name = 'apps/card_block/add.html'


class UpdatePersonView(UpdateView):
    queryset = User.objects.all()
    form_class = UserForm
    success_url = reverse_lazy('home')
    template_name = 'apps/card_block/edit.html'


class DeletePersonView(DeleteView):
    queryset = User.objects.all()
    success_url = reverse_lazy('home')
    template_name = 'apps/card_block/delete.html'
