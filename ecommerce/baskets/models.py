from django.db import models
from customers.models import Customer
from products.models import Product
from baskets import enums
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel


class Basket(BaseAbstractModel):
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"), null=True, on_delete=models.SET_NULL)
    status = models.CharField(choices=enums.Status.choices,  max_length=20, verbose_name=_("Status"))

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

    def __str__(self):
        return f"{self.customer} - {self.status}"


class BasketItem(BaseAbstractModel):
    basket = models.ForeignKey(Basket, verbose_name=_("Basket"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))
    price = models.DecimalField(max_digits=10, verbose_name=_("Price"), decimal_places=2)

    class Meta:
        verbose_name = _("basket item")
        verbose_name_plural = _("basket items")

    def __str__(self):
        return f"{self.basket} - {self.product} - {self.quantity} - {self.price}"