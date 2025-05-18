from django.urls import path
from . import views

urlpatterns = [
    path('mobiles/', views.mobile_list, name='mobile_list'),
    path('laptops/', views.laptop_list, name='laptop_list'),
    path('tvs/', views.tv_list, name='tv_list'),
]