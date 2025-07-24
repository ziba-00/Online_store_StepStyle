from django.contrib import admin
from products.models import Product, Category
from django.contrib import admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

