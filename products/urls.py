from django.urls import path

from products.views import index, contacts, woman, man, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('woman/', woman, name='woman'),
    path('man/', man, name='man'),
    path('<int:product_id>/', product_detail, name='product_detail'),
]
