from django.urls import path
from . import views  # Import the views from the current app

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),  # Register URL mapped to the register view
    path('login/', views.user_login, name='login'),      # Login URL
    path('tenants/', views.tenant_list, name='tenant_list'),
    path('properties/', views.property_list, name='property_list'),
    path('add-tenant/', views.add_tenant, name='add_tenant'),
    path('add-property/', views.add_property, name='add_property'),
    path('billings/', views.billing_list, name='billing_list'),
    path('add-billing/', views.add_billing, name='add_billing'),  # URL for adding billing records
    path('add-payment/', views.add_payment, name='add_payment'), # This should point to the index view
]
