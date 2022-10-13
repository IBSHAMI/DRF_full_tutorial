from django.urls import path

from .views import (
    ProductDetailAPIView,
    ProductListCreateAPIView,
    ProductUpdateAPIView,
    products_all_views,
)

app_name = 'products'

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
]
