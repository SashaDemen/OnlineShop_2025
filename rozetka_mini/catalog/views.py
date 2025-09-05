from django_filters.views import FilterView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django_render_block import render_block_to_string
from .models import Product
from .filters import ProductFilter

class ProductListView(FilterView):
    model = Product
    template_name = "catalog/product_list.html"
    paginate_by = 24
    filterset_class = ProductFilter
    queryset = Product.objects.select_related("category","shop").all().order_by("-created_at")

    def render_to_response(self, context, **kwargs):
        if self.request.headers.get("HX-Request"):
            html = render_block_to_string("catalog/product_list.html", "products", context)
            return HttpResponse(html)
        return super().render_to_response(context, **kwargs)

def product_detail(request, slug):
    product = get_object_or_404(Product.objects.select_related("shop","category"), slug=slug, is_active=True)
    return render(request, "catalog/product_detail.html", {"product": product})
