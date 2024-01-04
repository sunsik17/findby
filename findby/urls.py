from django.urls import path

from . import views

app_name = 'findby'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/product', views.register_product, name='register_product'),
]
