from django.urls import path
from . import views  # Import views from the current app
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    # Default and main pages
    path('', views.landing_page, name='landing_page'),  # Landing page
    path('index/', views.index, name='index'),  # Main page after login

    # Authentication
    path('register/', views.register, name='register'),  # Registration
    path('login/', views.user_login, name='login'),      # Login
    path('logout/', views.user_logout, name='logout'),   # Logout

    # Tenant management
    path('tenants/', views.tenant_list, name='tenant_list'),  # View all tenants
    path('add-tenant/', views.add_tenant, name='add_tenant'),  # Add a tenant

    # Property management
    path('properties/', views.property_list, name='property_list'),  # View all properties
    path('add-property/', views.add_property, name='add_property'),  # Add a property

    # Billing and payments
    path('billings/', views.billing_list, name='billing_list'),  # View all billing records
    path('add-billing/', views.add_billing, name='add_billing'),  # Add a billing record
    path('add-payment/', views.add_payment, name='add_payment'),  # Record a payment
]
