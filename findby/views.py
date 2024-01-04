from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from findby.form import SearchForm
from findby.models import Product


# Create your views here.
def index(request):
    page = request.GET.get('page', '1')
    products: [] = Product.objects.order_by('-create_date')
    paginator: Paginator = Paginator(products, 10)  # page당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'products': page_obj}

    return render(request, 'findby/products.html', context)


def register_product(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            print(form)
            return redirect('findby:index')
    else:
        form = SearchForm()

    context = {'form': form}

    return render(request, 'findby/products.html', context)
