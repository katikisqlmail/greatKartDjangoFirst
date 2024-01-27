from django.contrib import admin
from .models import Product ##.model --> models file within same App

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ('product_name',)
    }
    list_display = ('product_name', 'stock', 'price', 'is_available', 'modified_date', 'category')
    

admin.site.register(Product, ProductAdmin)

