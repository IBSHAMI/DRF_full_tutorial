from django.urls import path

from .views import (
    ProductDetailAPIView,
)

app_name = 'products'

urlpatterns = [
    path('<int:id>/', ProductDetailAPIView.as_view(), name='product_detail'),
]
