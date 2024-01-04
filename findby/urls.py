from django.urls import path

from . import views

app_name = 'find_kream_product'

urlpatterns = [
    path('', views.index, name='index'),
]
