from django.contrib import admin
from django.urls import path, include
from manager import views
from django.contrib.auth import views as auth_views  # Import auth views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page
    path('', include('manager.urls')),  # Include app's URLs
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('index/', views.index, name='index'),  # Main page
    


    # Authentication views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # App-specific URLs
    path('', include('manager.urls')),  # Includes all URLs defined in manager.urls
]