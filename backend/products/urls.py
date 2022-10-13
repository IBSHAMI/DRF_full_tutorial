from django.urls import path

from .views import (
    ProductDetailAPIView,
    ProductListCreateAPIView,
)

app_name = 'products'

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='product_create'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
]
