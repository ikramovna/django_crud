from django.urls import path

from apps.contact_list.views import home, add_person, update_person, delete_person

urlpatterns = [
    path('', home, name='home'),
    path('add', add_person, name='add'),
    path('update/<int:pk>', update_person, name='update'),
    path('delete/<int:pk>', delete_person, name='delete')

]
