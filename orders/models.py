from django.db import models
from django.contrib.auth import get_user_model
#from django.utils import timezone


from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User, related_name='orders', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    Address = models.CharField(max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Order {self.id} by {self.user}'
