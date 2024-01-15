from django.conf.urls.static import static

from schoolstore import settings
from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register,name='register'),
    path('Details', views.Details,name='Details'),


    ]
