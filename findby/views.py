from typing import Union, List

import django.forms
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from findby.form import SearchProductForm
from findby.model_builder import ProductBuilder
from findby.models import Product
from findby.simp_crawling import simp_crawling

__DEFAULT_PAGE_NUM = "1"


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    page: Union[str, None] = request.GET.get('page')
    search_category: Union[str, None] = request.GET.get('search_category')

    products = Product.objects.all().order_by('-create_date')
    if search_category:
        products = products.filter(category=search_category)
    context = __get_context(products, page, search_category)

    return render(request, 'findby/products.html', context)


def search_product(request: HttpRequest) -> HttpResponse:
    form = SearchProductForm(request.POST or None)

    if form.is_valid():
        data = simp_crawling(words=form.content, category=form.category)
        if __data_is_valid(data):
            __to_product(data)

    return redirect('findby:index')

def delete_products(request):
    if request.method == 'POST':
        print(request.POST)
        # if form:
        #     print(form)
        #     raise

    return redirect('findby:index')


def __to_product(product_info: [str]) -> None:
    brand = product_info[1]
    name = product_info[2]
    amount = product_info[5]
    category = product_info[len(product_info) - 2]
    link = product_info[len(product_info) - 1]

    product = (ProductBuilder()
               .set_name(name)
               .set_price(amount)
               .set_category(category)
               .set_brand(brand)
               .set_link(link)
               .build())

    product.save()


def __data_is_valid(data: str) -> bool:
    if not data:
        return False
    return True


def __get_context(products: List[Product], page: Union[str, None], search_category: str) -> dict:
    paginator: Paginator = Paginator(products, 10)  # page당 10개씩 보여주기
    page_obj: Paginator = paginator.get_page(page)
    return {
        'products': page_obj,
        'search_category': search_category
    }
