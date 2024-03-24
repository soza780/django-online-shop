from django.contrib import admin

from .models import Product, Category


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available',]
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'available',]
    prepopulated_fields = {'slug': ('name',)}
