from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tenant, Property, Billing, Payment, Notification, LeaseAgreement, AdminAction, Report

admin.site.register(Tenant)
admin.site.register(Property)
admin.site.register(Billing)
admin.site.register(Payment)
admin.site.register(Notification)
admin.site.register(LeaseAgreement)
admin.site.register(AdminAction)
admin.site.register(Report)
