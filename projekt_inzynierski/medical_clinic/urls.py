from django.urls import path
from django.conf.urls import include, url
from . import views
from .views import MedicHomePage, RecepcjaHomePage
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/medic', MedicHomePage.as_view(), name='medic_home'),
    path('home/recepcja', RecepcjaHomePage.as_view(), name='recepcja_home'),
]