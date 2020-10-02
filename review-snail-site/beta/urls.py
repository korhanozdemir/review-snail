from django.urls import path

from . import views

urlpatterns = [
    path('beta', views.upload, name='upload'),
    path('', views.index, name='index'),

]