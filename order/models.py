from django.db import models
from base.models import TimeStampedModel
from product.models import Product

from django.contrib.auth import get_user_model

User = get_user_model()


class OrderItem(TimeStampedModel):
    customer = models.ForeignKey(User, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2 , null=True , blank=True)
    ordered = models.BooleanField(default=False)
    order = models.ForeignKey("Order", models.CASCADE , related_name="order_item")


    def __str__(self):
        return self.product.title

    def set_total_price(self):
        self.total_price = self.product.price * self.quantity
        self.save()
        return

class Order(TimeStampedModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=20, decimal_places=2 , null=True , blank= True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.username

    # def set_total_price(self):
    #     for price in self.order_item.objects.all() :
    #         self.total_price += price.total_price
    #     self.save()
    #     return
    #



