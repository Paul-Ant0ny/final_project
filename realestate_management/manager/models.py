from django.db import models

# Create your models here.
from django.db import models

# 1. Tenant Model
class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.email}"

# 2. Property Model
class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    owner = models.CharField(max_length=100)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.address}"

# 3. Billing Model
class Billing(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Bill for {self.tenant.name} - {self.property.name}"

# 4. Payment Model
class Payment(models.Model):
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount_paid} for {self.billing.tenant.name}"

# 5. Notification Model (Optional)
class Notification(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification to {self.tenant.name} at {self.sent_at}"

# 6. Lease Agreement Model (Optional)
class LeaseAgreement(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    terms = models.TextField()

    def __str__(self):
        return f"Lease for {self.tenant.name} - {self.property.name}"

# 7. Admin Action Model (Optional)
class AdminAction(models.Model):
    admin_user = models.CharField(max_length=100)
    action = models.TextField()
    action_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admin_user} performed {self.action} at {self.action_time}"

# 8. Report Model (Optional)
class Report(models.Model):
    report_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.report_type} Report at {self.created_at}"
