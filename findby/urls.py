from django.urls import path

from . import views

app_name = 'findby'

urlpatterns = [
    path('', views.index, name='index'),
]
