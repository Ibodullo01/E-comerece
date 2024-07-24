from django.urls import path
from  order.api.v0.views import *

app_name = 'api_order'

urlpatterns = [
    path('order_item/' , OrderItemApiView.as_view(), name='order_item'),
    path('order/' , OrderApiView.as_view(), name='order'),
    path('order_item-create/' , OrderItemCreateApiView.as_view(), name='order_item_create'),
    path('cart/' ,  CardByOwnerListApiView.as_view(), name='cart'),

]