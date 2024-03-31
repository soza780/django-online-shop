from django.urls import path
from . import views

app_name = 'coupons'

urlpatterns = [
    path('add/', views.coupon_add, name='apply'),
]
