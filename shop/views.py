from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from shop.models import Shop
from shop.serializers import ShopSerializer

from order.producer import publish

class ShopViewSet(viewsets.ViewSet):

    def list(self, request):
        shops = Shop.objects.all()

        serializer = ShopSerializer(shops, many=True)

        publish()

        return Response(serializer.data)

    def create(self, request):
        serializer = ShopSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        shop = Shop.objects.get(id=pk)

        serializer = ShopSerializer(instance=shop, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        shop = Shop.objects.get(id=pk)

        serializer = ShopSerializer(shop)

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        shop = Shop.objects.get(id=pk)

        shop.delete()

        return Response(status=status.HTTP_200_OK)