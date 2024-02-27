from django.shortcuts import render
from rest_framework import viewsets

class OrderViewSet(viewsets.ViewSet):

    def list(self, request):
        pass

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def retrieve(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass