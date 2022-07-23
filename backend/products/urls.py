from django.urls import path
from .views import (
    ProductDetailAPIView,
)
    
app_name = "products"

urlpatterns = [
    path('product_detail/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
]
