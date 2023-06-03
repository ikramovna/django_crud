from django.urls import path

from apps.team_list.views import HomeListView, AddPersonView, UpdatePersonView, DeletePersonView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('add', AddPersonView.as_view(), name='add'),
    path('update/<int:pk>', UpdatePersonView.as_view(), name='update'),
    path('delete/<int:pk>', DeletePersonView.as_view(), name='delete')
]
