from django.urls import path
from .views import (
    ProductCreateAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
)
    
app_name = "products"

urlpatterns = [
    path('', ProductCreateAPIView.as_view(), name='create'),
    path('products_list/', ProductListAPIView.as_view(), name='products_list'),
    path('product_detail/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
]
