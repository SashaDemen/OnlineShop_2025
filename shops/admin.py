from django.contrib import admin
from .models import Shop
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display=('name','owner','rating_avg','rating_count','created_at')
    prepopulated_fields={'slug':('name',)}
