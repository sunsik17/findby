from typing import Union, List

from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from findby.form import SearchForm
from findby.model_builder import ProductBuilder
from findby.models import Product
from findby.simp_crawling import simp_crawling


__DEFAULT_PAGE_NUM = "1"


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    page: Union[str, None] = request.GET.get('page', __DEFAULT_PAGE_NUM)
    category: Union[str, None] = request.GET.get('category', "")
    if category != "":
        products: List[Product] = Product.objects.filter(category=category).order_by('-create_date')
    else:
        products: List[Product] = Product.objects.order_by('-create_date')

    context = __get_context(products, page)

    return render(request, 'findby/products.html', context)


def search_product(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            data = simp_crawling(words=content)
            if __data_is_valid(data):
                __to_product(data)
            return redirect('findby:index')
    else:
        form = SearchForm()

    context = {'form': form}

    return render(request, 'findby/products.html', context)


def delete_products(request):
    if request.method == 'POST':
        print(request.POST)
        # if form:
        #     print(form)
        #     raise

    return redirect('findby:index')


def __to_product(data: str) -> None:
    product_info = data.split("\n")
    brand = product_info[1]
    name = product_info[2]
    amount = product_info[5]

    product = (ProductBuilder()
               .set_name(name)
               .set_price(amount)
               .set_category("신발")
               .set_brand(brand)
               .build())

    product.save()


def __data_is_valid(data: str) -> bool:
    if not data:
        return False
    return True


def __get_context(products: List[Product], page: Union[str, None]) -> dict:
    paginator: Paginator = Paginator(products, 10)  # page당 10개씩 보여주기
    page_obj: Paginator = paginator.get_page(page)
    return {'products': page_obj}
