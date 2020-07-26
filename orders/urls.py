from django.urls import path
from .views import order_list, order

urlpatterns = [
    path('', order_list, name="order_list"),
    path('new', order, name="order")]
