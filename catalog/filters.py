import django_filters
from .models import Product, Category

class ProductFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method="search", label="Пошук")
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte", label="Від ціни")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte", label="До ціни")
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ["category", "min_price", "max_price"]

    def search(self, queryset, name, value):
        return queryset.filter(is_active=True).filter(title__icontains=value) | queryset.filter(description__icontains=value)
