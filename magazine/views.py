from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.select_related('category').prefetch_related('tags')
    return render(request, 'magazine/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'magazine/product_detail.html', {'product': product})



def index(request):
    return render(request, 'magazine/index.html')