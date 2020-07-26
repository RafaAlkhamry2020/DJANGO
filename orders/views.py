from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Order
from .forms import AddAddress
from .utils import send_order_email


@login_required
def order(request):
    user = request.user

    if not user.cart.items.exists():
        return redirect('product_list')

    if request.method == 'POST':
        form = AddAddress(request.POST, request.FILES)

        if form.is_valid():
            order = form.save(user)
            send_order_email(user, order)
            return render(request, 'orders/order-successful.html')
        else:
            form = AddAddress()

        return render(request, 'orders/order.html', {'form': form})


def order_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.all()
        #orders = Order.objects.filter(user=request.user)
        return render(request, 'orders/order_list.html', {'orders': orders})
    else:
        return redirect('products-list')
