from django.contrib import admin

# Register your models here.
from .models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name','price','digital']
    
