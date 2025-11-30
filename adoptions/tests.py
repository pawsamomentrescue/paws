from __future__ import annotations

from datetime import date

from django.test import Client, TestCase
from django.urls import reverse

from .models import Animal


class AdoptionsViewsTests(TestCase):
    def setUp(self) -> None:
        self.animal = Animal.objects.create(
            name="Buddy",
            slug="buddy",
            species="Dog",
            intake_date=date.today(),
        )

    def test_animal_list_view(self) -> None:
        client = Client()
        response = client.get(reverse("adoptions:animal_list"))
        self.assertEqual(response.status_code, 200)

    def test_animal_detail_view(self) -> None:
        client = Client()
        response = client.get(reverse("adoptions:animal_detail", args=[self.animal.slug]))
        self.assertEqual(response.status_code, 200)
