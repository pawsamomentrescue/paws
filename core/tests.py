from __future__ import annotations

from django.test import Client, TestCase
from django.urls import reverse


class CoreViewsTests(TestCase):
    def test_home_page_renders(self) -> None:
        client = Client()
        response = client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/home.html")
