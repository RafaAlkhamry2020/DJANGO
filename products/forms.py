from django.forms import ModelForm
from .models import product


class AddProductForm(ModelForm):
    class Meta:
        model = product
        fields = ('brand', 'title', 'description', 'price', 'image')
