from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.OneToOneField(
        User, related_name='orders', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    updateed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
