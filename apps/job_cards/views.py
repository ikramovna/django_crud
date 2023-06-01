from django.shortcuts import render, redirect

from apps.job_cards.forms import UserForm
from apps.job_cards.models import User


def home(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'apps/job_cards/index.html', context)


def add_person(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'apps/job_cards/add.html')


def update_person(request, pk):
    users = User.objects.get(id=pk)
    context = {'request': request, 'form': UserForm(), 'users': users}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.filter(id=pk).update(**form.cleaned_data)
        return redirect('/')
    return render(request, 'apps/job_cards/edit.html', context)


def delete_person(request, pk):
    users = User.objects.filter(id=pk)
    users.delete()
    return redirect('/')
