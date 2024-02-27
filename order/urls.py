from django.urls import path
from order.views import OrderViewSet

urlpatterns = [
    path('', OrderViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<str:pk>', OrderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
