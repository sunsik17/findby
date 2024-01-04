from django.core.paginator import Paginator
from django.shortcuts import render

from findby.models import Product


# Create your views here.
def index(request):
    page = request.GET.get('page', '1')
    products: [] = Product.objects.order_by('-create_date')
    paginator: Paginator = Paginator(products, 10)  # page당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'products': page_obj}
    return render(request, 'findby/products.html', context)
