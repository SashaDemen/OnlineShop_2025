from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import SellerReview
from orders.models import Order

@login_required
def create_review(request, order_id):
    order = get_object_or_404(Order, id=order_id, buyer=request.user, status=Order.Status.DELIVERED)
    if request.method == "POST":
        rating = int(request.POST.get("rating", 5))
        text = request.POST.get("text", "")
        SellerReview.objects.create(order=order, seller=order.shop, author=request.user, rating=rating, text=text)
        return redirect("/")
    return render(request, "reviews/create_review.html", {"order": order})
