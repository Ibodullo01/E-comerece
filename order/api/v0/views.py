from django.contrib import messages
from rest_framework.response import Response
from order.models import Order

from .serializers import *
from rest_framework import generics, status

class CardByOwnerListApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(customer=self.request.user , ordered=False)
        return qs








class OrderItemApiView(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class OrderApiView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderItemCreateApiView(generics.CreateAPIView):
    serializer_class = OrderItemCreateSerializer
    queryset = OrderItem.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderItemDeleteApiView(generics.DestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

    def delete(self, pk):
        order =OrderItem.objects.get(pk=pk)
        order.delete()
        messages.info("Deleted Order successfully")
