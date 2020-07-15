from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
from .models import product
from .forms import AddProductForm
# Create your views here.


def product_list(request):
    products = product.objects.all()
    return render(request, 'products/products-list.html',
                  {'products': products})


def product_detalis(request, pk):
    Product = get_object_or_404(product, pk=pk)
    return render(request, 'products/product-detalis.html',
                  {'Product': Product})


# @login_required
def product_add(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = AddProductForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return render(request, 'products/products-add-successful.html')
        else:
            form = AddProductForm()
        return render(request, 'products/products-add.html', {'form': form})
    else:
        return redirect('product_list')


def product_edit(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        Product = get_object_or_404(product, pk=pk)

        if request.method == 'POST':
            form = AddProductForm(
                request.POST, request.FILES, instance=Product)

            if form.is_valid():
                form.save()
                return render(request, 'products/products-add-successful.html')
        else:
            form = AddProductForm(instance=Product)
        return render(request, 'products/products-add.html', {'form': form})
    else:
        return redirect('product_list')


def product_delete(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        Product = get_object_or_404(product, pk=pk)
        Product.delete()
        return redirect('product_list')
    else:
        return redirect('product_list')
