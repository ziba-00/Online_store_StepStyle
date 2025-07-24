from django.shortcuts import render

from .models import Product
from news.models import News

def index(request):
    products = Product.objects.filter(is_active=True)
    news = News.objects.order_by('-created_at')
    return render(request, 'index.html', context={
        'products': products,
        'news': news,
    })


def contacts(request):
    return render(request, 'contacts.html')

def woman(request):
   products = Product.objects.filter(category__title='woman', is_active=True)
   return render(request, 'index.html', context={'products': products})

def man(request):
   products = Product.objects.filter(category__title='man', is_active=True)
   return render(request, 'index.html', context={'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', context={'product': product})
