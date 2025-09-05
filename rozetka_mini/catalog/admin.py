from django.contrib import admin
from .models import Category, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ("name","parent")

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title","shop","price","stock","is_active","category")
    list_filter = ("shop","category","is_active")
    prepopulated_fields = {"slug":("title",)}
    inlines = [ProductImageInline]
