from django.db import models

class Order(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "Нове"
        PAID = "paid", "Оплачене"
        SHIPPED = "shipped", "Відправлене"
        DELIVERED = "delivered", "Доставлене"
        CANCELED = "canceled", "Скасоване"

    buyer = models.ForeignKey("accounts.User", on_delete=models.PROTECT, related_name="orders")
    shop = models.ForeignKey("shops.Shop", on_delete=models.PROTECT, related_name="orders")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.NEW)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("catalog.Product", on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    qty = models.PositiveIntegerField()
