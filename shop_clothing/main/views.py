from django.shortcuts import render
from main.models import Products, Price


def index(request):
    return render(request, 'main/html/index.html')


def products(request):
    product = Products.objects.all()
    data = {"products": product}
    return render(request, 'main/html/products.html', data)


def product_detail(request, category_slug, product_slug):
    single_product = Products.objects.get(category__slug=category_slug, slug=product_slug)
    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product.html', context)
