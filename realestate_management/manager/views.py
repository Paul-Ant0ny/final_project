from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tenant, Property, Billing
from .forms import TenantForm, PropertyForm, BillingForm, PaymentForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model


# Landing page
def landing_page(request):
    return render(request, 'landing.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')  # Capture the email from the form

            # Send welcome email
            send_mail(
                subject='Welcome to Real Estate Management System',
                message=f'Hi {username},\n\nThank you for registering with our platform. We are excited to have you onboard!\n\nBest regards,\nReal Estate Management Team.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )

            messages.success(request, 'Your account has been created successfully! A welcome email has been sent to your email address.')
            return redirect('login')  # Redirect to login page
        else:
            messages.error(request, 'There was an issue with your registration. Please correct the errors below.')
    else:
        form = UserCreationForm()  # Render an empty form for GET requests

    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # Authenticate user
        if user is not None:
            login(request, user)  # Log in the user
            messages.success(request, 'Login successful.')
            return redirect('index')  # Redirect to main page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')


# Logout view
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('landing_page')


# Home page (main dashboard)
@login_required
def index(request):
    return render(request, 'manager/index.html')


# Add a new tenant
@login_required
def add_tenant(request):
    if request.method == "POST":
        form = TenantForm(request.POST)
        if form.is_valid():
            tenant = form.save()

            # Send email notification to the tenant
            send_mail(
                subject='Welcome to Real Estate Management',
                message=f'Hello {tenant.name},\n\nYou have been successfully added as a tenant in our system. Please feel free to contact us for any inquiries.\n\nBest regards,\nReal Estate Management Team.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[tenant.email],  # Ensure the Tenant model has an email field
                fail_silently=False,
            )

            messages.success(request, 'Tenant added successfully and notification sent.')
            return redirect('tenant_list')
    else:
        form = TenantForm()
    return render(request, 'manager/add_tenant.html', {'form': form})


# List all tenants
@login_required
def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'manager/tenant_list.html', {'tenants': tenants})


# Add a new property
@login_required
def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property added successfully.')
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'manager/add_property.html', {'form': form})


# List all properties
@login_required
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'manager/property_list.html', {'properties': properties})


# Add a new billing record
@login_required
def add_billing(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            billing = form.save()

            # Notify tenant of billing
            send_mail(
                subject='New Billing Statement',
                message=f'Dear {billing.tenant.name},\n\nA new billing statement has been generated for your account. Please log in to your portal to view the details.\n\nBest regards,\nReal Estate Management Team.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[billing.tenant.email],  # Ensure Billing model links to a Tenant with an email field
                fail_silently=False,
            )

            messages.success(request, 'Billing record added successfully and tenant notified.')
            return redirect('billing_list')
    else:
        form = BillingForm()
    return render(request, 'manager/add_billing.html', {'form': form})


# List all billing records
@login_required
def billing_list(request):
    billings = Billing.objects.all()
    return render(request, 'manager/billing_list.html', {'billings': billings})


# Add a new payment
@login_required
def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()

            # Notify tenant of payment receipt
            send_payment_notification(
                user_email=payment.tenant.email,  # Ensure the Payment model links to a Tenant with an email field
                tenant_name=payment.tenant.name,
                payment_amount=payment.amount,
                payment_date=payment.date,
            )

            messages.success(request, 'Payment recorded successfully and tenant notified.')
            return redirect('billing_list')
    else:
        form = PaymentForm()
    return render(request, 'manager/add_payment.html', {'form': form})


# Function to send email notification
def send_payment_notification(user_email, tenant_name, payment_amount, payment_date):
    subject = 'Payment Received - Real Estate Management'
    message = f"Hello {tenant_name},\n\nWe have received your payment of ${payment_amount} on {payment_date}. Thank you for your payment.\n\nBest regards,\nReal Estate Management Team."
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, from_email, [user_email])
