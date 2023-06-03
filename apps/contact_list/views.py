from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from apps.contact_list.forms import UserForm
from apps.contact_list.models import User


def home(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'apps/contact_list/index.html', {'users': users})


def add_person(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'apps/contact_list/add.html')


def update_person(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'user': user}
    return render(request, 'apps/contact_list/edit.html', context)


def delete_person(request, pk):
    user = User.objects.filter(id=pk)
    user.delete()
    return redirect('/')
