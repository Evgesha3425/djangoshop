
from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('catalog/', catalog, name='catalog'),
    path('goods/<int:good>/<str:adik>', all_goods)
]
