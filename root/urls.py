from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job_cards', include('apps.job_cards.urls')),
    path('team_list/', include('apps.team_list.urls')),
    path('customers_list/', include('apps.customers_list.urls')),
    path('news/', include('apps.news.urls')),
    path('card_location/', include('apps.card_location.urls')),
    path('job_categories/', include('apps.job_categories.urls')),
    path('card_block/', include('apps.card_block.urls')),
    path('contact_list/', include('apps.contact_list.urls')),
    path('order_placed/', include('apps.order_placed.urls')),
    path('simple_job/', include('apps.simple_job.urls')),



] + static(MEDIA_URL, document_root=MEDIA_ROOT)
