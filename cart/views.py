from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product

def _get_cart(session):
    cart = session.get("cart")
    if not cart:
        cart = {"items": {}, "count": 0}
        session["cart"] = cart
    return cart

def cart_view(request):
    cart = _get_cart(request.session)
    items = []
    total = 0
    for pid, qty in cart["items"].items():
        product = Product.objects.filter(id=pid, is_active=True).first()
        if product:
            subtotal = product.price * qty
            total += subtotal
            items.append({"product": product, "qty": qty, "subtotal": subtotal})
    return render(request, "cart/cart.html", {"items": items, "total": total})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_active=True)
    qty = int(request.POST.get("qty", 1))
    if qty < 1: qty = 1
    if qty > product.stock: qty = product.stock
    cart = _get_cart(request.session)
    cart["items"][str(product.id)] = cart["items"].get(str(product.id), 0) + qty
    cart["count"] = sum(cart["items"].values())
    request.session.modified = True
    if request.headers.get("HX-Request"):
        return HttpResponse(str(cart["count"]))
    return redirect("cart_view")

def remove_from_cart(request, product_id):
    cart = _get_cart(request.session)
    cart["items"].pop(str(product_id), None)
    cart["count"] = sum(cart["items"].values())
    request.session.modified = True
    return redirect("cart_view")
