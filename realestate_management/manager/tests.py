from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

class AddPaymentViewTests(TestCase):
    def test_add_payment_view(self):
        response = self.client.get(reverse('add_payment'))
        self.assertEqual(response.status_code, 200)

def send_test_email():
    send_mail(
        subject='Test Email',
        message='This is a test email from Django!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['paulantony360@gmail.com.com'],  # Replace with the recipient's email
        fail_silently=False,
    )
        

