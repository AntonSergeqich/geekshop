from django.conf import settings
from django.db import models

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)
    price = models.PositiveIntegerField(verbose_name='цена', default=0)
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='время')

    @property
    def cost(self):
        return self.product.price * self.quantity

    @property
    def total_q(self):
        _items = Basket.objects.filter(user=self.user)
        _tq = sum(list(map(lambda x: x.quantity, _items)))
        return _tq

    @property
    def all_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.price, _items)))
        return _total_cost
