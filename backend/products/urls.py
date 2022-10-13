from django.urls import path

from .views import (
    ProductDetailAPIView,
    ProductListCreateAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
    products_all_views,
    ProductGenericAPIView,
)

app_name = 'products'

urlpatterns = [
    path('', ProductGenericAPIView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product_delete'),
    path('<int:pk>/', ProductGenericAPIView.as_view(), name='product_detail'),
]
