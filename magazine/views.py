from django.shortcuts import render, get_object_or_404
from .models import Product, Model1, Model2


def product_list(request):
    products = Product.objects.select_related('category').prefetch_related('tags')
    return render(request, 'magazine/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'magazine/product_detail.html', {'product': product})


def model1_list(request):
    model1_items = Model1.objects.all()
    return render(request, 'magazine/model1_list.html', {'model1_list': model1_items})


def model1_detail(request, model1_id):
    model1 = get_object_or_404(Model1, pk=model1_id)
    return render(request, 'magazine/model1_detail.html', {'model1': model1})


def model2_list(request):
    model2_items = Model2.objects.all()
    return render(request, 'magazine/model2_list.html', {'model2_list': model2_items})


def model2_detail(request, model2_id):
    model2 = get_object_or_404(Model2, pk=model2_id)
    return render(request, 'magazine/model2_detail.html', {'model2': model2})


def index(request):
    return render(request, 'magazine/index.html')
