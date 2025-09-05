from django.contrib import admin
from .models import SellerReview
@admin.register(SellerReview)
class SellerReviewAdmin(admin.ModelAdmin):
    list_display=('seller','author','rating','created_at')
    list_filter=('seller','rating')
