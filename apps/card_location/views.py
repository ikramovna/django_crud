from django.shortcuts import render, redirect

from apps.card_location.forms import UserForm
from apps.card_location.models import User


def home(request):
    user = User.objects.all()
    context = {
        'users': user
    }
    return render(request, 'apps/card_location/index.html', context)


def add_person(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'apps/card_location/add.html')


def update_person(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'user': user}
    return render(request, 'apps/card_location/edit.html', context)


def delete_person(request, pk):
    user = User.objects.filter(id=pk)
    user.delete()
    return redirect('/')
