from django.contrib import admin
from django.urls import path, include
from manager import views
from django.contrib.auth import views as auth_views  # Import auth views



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', auth_views.LoginView.as_view(), name='login'),      # Login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),   # Logout page
    path('', include('manager.urls')),
    path('tenants/', views.tenant_list, name='tenant_list'),
    path('properties/', views.property_list, name='property_list'),
    path('billings/', views.billing_list, name='billing_list'),# This connects the app's URLs
]
