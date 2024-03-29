from typing import Union, List

from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from findby.form import SearchProductForm, DeleteProductIdsForm
from findby.models import Product
from findby.simp_crawling import simp_crawling


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    page: Union[str, None] = request.GET.get('page')
    search_category: Union[str, None] = request.GET.get('search_category')

    products = Product.objects.all().order_by('-create_date')
    if search_category:
        products = products.filter(category=search_category)
    context = __set_index_page_products_context(products, page, search_category)

    return render(request, 'findby/products.html', context)


def search_product(request: HttpRequest) -> HttpResponse:
    form = SearchProductForm(request.POST)
    if form.is_valid():
        product_dto = simp_crawling(words=form.cleaned_data['contents'], category=form.cleaned_data['category'])
        product = Product().from_dto(dto=product_dto)
        product.save()

    return redirect('findby:index')


def delete_products(request):
    form = DeleteProductIdsForm(request.POST)
    if form.is_valid():
        product_ids: [] = form.cleaned_data['selected_products'].split(',')
        Product.objects.filter(id__in=product_ids).delete()

    return redirect('findby:index')


def __set_index_page_products_context(products: List[Product], page: Union[str, None], search_category: str) -> dict:
    paginator: Paginator = Paginator(products, 10)  # page당 10개씩 보여주기
    page_obj: Paginator = paginator.get_page(page)
    return {
        'products': page_obj,
        'search_category': search_category
    }
