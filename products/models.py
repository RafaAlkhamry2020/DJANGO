from django.db import models
from django.urls import reverse
#from django.utils import timezone


# Create your models here.


class Product (models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('product_detalis', args=(self.id,))

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super().delete(*args, **kwargs)
