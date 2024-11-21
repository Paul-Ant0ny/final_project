from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tenant, Property, Billing
from .forms import TenantForm, PropertyForm, BillingForm, PaymentForm
from django.contrib.auth.views import LoginView

# Registration view
def register(request):
    if request.method == 'POST':  # Handle form submission
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the new user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login page after registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()  # If it's a GET request, show the form

    return render(request, 'registration/register.html', {'form': form})
  
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # Authenticate user
        if user is not None:
            login(request, user)  # Log the user in
            messages.success(request, 'Login successful.')
            return redirect('index')  # Redirect to the main page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

# Add a new tenant
@login_required
def add_tenant(request):
    if request.method == "POST":
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')  # Redirect to tenant list after adding tenant
        else:
            print(form.errors)  # Debugging form errors
    else:
        form = TenantForm()
    return render(request, 'manager/add_tenant.html', {'form': form})


# Add a new property
@login_required
def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')  # Redirect to property list
    else:
        form = PropertyForm()
    return render(request, 'manager/add_property.html', {'form': form})


# Add a new billing record
@login_required
def add_billing(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('billing_list')  # Redirect to billing list
    else:
        form = BillingForm()
    return render(request, 'manager/add_billing.html', {'form': form})


# Add a new payment
@login_required
def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('billing_list')  # Redirect to billing list after payment
    else:
        form = PaymentForm()
    return render(request, 'manager/add_payment.html', {'form': form})


# List all tenants
@login_required
def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'manager/tenant_list.html', {'tenants': tenants})


# List all properties
@login_required
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'manager/property_list.html', {'properties': properties})


# List all billing records
@login_required
def billing_list(request):
    billings = Billing.objects.all()
    return render(request, 'manager/billing_list.html', {'billings': billings})


# Home page
def index(request):
    return render(request, 'manager/index.html')
