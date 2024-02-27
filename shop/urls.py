from django.urls import path
from shop.views import ShopViewSet

urlpatterns = [
    path('', ShopViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<str:pk>', ShopViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
