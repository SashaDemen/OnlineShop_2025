from django.db import models
class SellerReview(models.Model):
    order = models.OneToOneField("orders.Order", on_delete=models.PROTECT)
    seller = models.ForeignKey("shops.Shop", on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True)
    rating = models.PositiveSmallIntegerField()
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
