from django.shortcuts import render, redirect

from apps.news.forms import UserForm
from apps.news.models import User


def home(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'apps/news_widget/index.html', context)


def add_person(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'apps/news_widget/add.html')


def update_person(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            User.objects.filter(id=pk).update(**form.cleaned_data)
        return redirect('home')
    context = {'user': user}
    return render(request, 'apps/news_widget/edit.html', context)


def delete_person(request, pk):
    User.objects.filter(id=pk).delete()
    return redirect('/')
