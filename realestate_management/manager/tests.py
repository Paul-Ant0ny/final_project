from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

class AddPaymentViewTests(TestCase):
    def test_add_payment_view(self):
        response = self.client.get(reverse('add_payment'))
        self.assertEqual(response.status_code, 200)