
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:pk>/', views.customer_record, name='customer'),  
    path('customer/<int:pk>/delete/', views.delete_customer, name='delete_customer'),
    path('customer/<int:pk>/edit/', views.edit_customer, name='edit_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),
]
