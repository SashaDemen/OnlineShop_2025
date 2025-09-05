from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from decimal import Decimal
from catalog.models import Product
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart = request.session.get("cart", {"items": {}})
    if request.method == "POST" and cart["items"]:
        with transaction.atomic():
            items_by_shop = {}
            for pid, qty in cart["items"].items():
                p = Product.objects.select_for_update().get(id=pid)
                items_by_shop.setdefault(p.shop_id, []).append((p, qty))
            for shop_id, prods in items_by_shop.items():
                total = sum(p.price * qty for p, qty in prods)
                order = Order.objects.create(buyer=request.user, shop_id=shop_id, total=total)
                for p, qty in prods:
                    if qty > p.stock: qty = p.stock
                    OrderItem.objects.create(order=order, product=p, price=p.price, qty=qty)
                    p.stock -= qty
                    p.save()
            request.session["cart"] = {"items": {}, "count": 0}
            request.session.modified = True
            return redirect("/")
    items_list = []
    total = Decimal("0")
    for pid, qty in cart["items"].items():
        try:
            p = Product.objects.get(id=pid)
            subtotal = p.price * qty
            items_list.append({"product": p, "qty": qty, "subtotal": subtotal})
            total += subtotal
        except Product.DoesNotExist:
            pass
    return render(request, "orders/checkout.html", {"items": items_list, "total": total})
