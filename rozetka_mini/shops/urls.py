from django.urls import path
from .views import my_shop, edit_shop
urlpatterns=[path('me/', my_shop, name='my_shop'), path('me/edit/', edit_shop, name='edit_shop')]
