from django.urls import path

from . import views

urlpatterns = [
    # base URL
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]