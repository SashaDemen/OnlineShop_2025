from django.db import models
from django.utils.text import slugify

class Shop(models.Model):
    owner = models.OneToOneField("accounts.User", on_delete=models.CASCADE, related_name="shop")
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="shops/avatars/", blank=True, null=True)
    banner = models.ImageField(upload_to="shops/banners/", blank=True, null=True)
    payment_info = models.JSONField(default=dict, blank=True)
    rating_avg = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    rating_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.name)
        super().save(*args, **kwargs)
