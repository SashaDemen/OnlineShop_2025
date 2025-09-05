from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Shop

@login_required
def my_shop(request):
    shop = getattr(request.user, "shop", None)
    return render(request, "shops/my_shop.html", {"shop": shop})

@login_required
def edit_shop(request):
    shop = getattr(request.user, "shop", None)
    if not shop:
        shop = Shop.objects.create(owner=request.user, name=f"Магазин {request.user.username}")
    if request.method == "POST":
        shop.name = request.POST.get("name", shop.name)
        shop.description = request.POST.get("description", shop.description)
        shop.payment_info = {"info": request.POST.get("payment_info", "")}
        shop.save()
        return redirect("my_shop")
    return render(request, "shops/edit_shop.html", {"shop": shop})
