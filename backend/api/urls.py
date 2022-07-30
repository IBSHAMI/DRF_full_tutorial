from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import api_home

app_name = 'api'

urlpatterns = [
    path('auth/', obtain_auth_token, name='auth'),
    path('', api_home, name='api_home'),
]