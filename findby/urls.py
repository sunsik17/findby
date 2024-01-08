from django.urls import path

from . import views

app_name = 'findby'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/product', views.search_product, name='search_product'),
    path('delete/products', views.delete_products, name='delete_products'),
    # path('?category=', views.find_by_category, name='find_by_category'),
]
