from django.urls import path
from .views import ProductListView, product_detail
urlpatterns=[path('', ProductListView.as_view(), name='catalog_list'), path('product/<slug:slug>/', product_detail, name='product_detail')]
