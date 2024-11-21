
from django import forms
from .models import Tenant, Property
from .models import Billing, Payment

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'email', 'phone', 'lease_start_date', 'lease_end_date']

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'owner', 'rent_amount']
        
class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['tenant', 'property', 'amount_due', 'due_date', 'paid']
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['payment_date']  # Exclude non-editable field

