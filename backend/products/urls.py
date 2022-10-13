from django.urls import path

from .views import (
    ProductDetailAPIView,
    ProductCreateAPIView,
)

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('create/', ProductCreateAPIView.as_view(), name='product_create'),
]
