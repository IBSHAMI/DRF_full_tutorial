from django.urls import path
from .views import (
    ProductListCreateAPIView,
    ProductDetailAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
)
    
app_name = "products"

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='create'),
    path('product_detail/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('product_update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_delete'),
]
