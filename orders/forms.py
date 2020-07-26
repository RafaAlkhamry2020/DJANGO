from django.forms import ModelForm
from .models import Order


class AddAddress(ModelForm):
    class Meta:
        model = Order
        fields = ('Address',)

    def save(self, user):
        self.instance.user = user
        self.instance.save()

        for item in user.cart.items.all():
            self.instance.items.add(item)

        user.cart.items.clear()

        return self.instance
