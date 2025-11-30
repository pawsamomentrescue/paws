from __future__ import annotations

from decimal import Decimal

from django.test import Client, TestCase
from django.urls import reverse

from .models import Donation


class DonationsViewsTests(TestCase):
    def test_get_donate_form(self) -> None:
        client = Client()
        response = client.get(reverse("donations:donate"))
        self.assertEqual(response.status_code, 200)

    def test_post_donation_creates_record(self) -> None:
        client = Client()
        response = client.post(
            reverse("donations:donate"),
            {
                "full_name": "Donor",
                "email": "donor@example.com",
                "amount": "10.00",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Donation.objects.count(), 1)
        donation = Donation.objects.get()
        self.assertEqual(donation.amount, Decimal("10.00"))
        self.assertEqual(donation.status, Donation.STATUS_SUCCEEDED)
