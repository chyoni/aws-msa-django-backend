from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from order.serializers import OrderSerializer
from order.models import Order

class OrderViewSet(viewsets.ViewSet):

    def list(self, request):
        orders = Order.objects.all()

        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = OrderSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        order = Order.objects.get(id=pk)

        serializer = OrderSerializer(instance=order, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        order = Order.objects.get(id=pk)

        serializer = OrderSerializer(order)

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        order = Order.objects.get(id=pk)

        order.delete()

        return Response(status=status.HTTP_200_OK)