from __future__ import annotations

from django.test import Client, TestCase
from django.urls import reverse

from .models import Story


class StoriesViewsTests(TestCase):
    def setUp(self) -> None:
        self.story = Story.objects.create(
            title="Test Story",
            slug="test-story",
            body="Body",
            is_published=True,
        )

    def test_story_list_view(self) -> None:
        client = Client()
        response = client.get(reverse("stories:story_list"))
        self.assertEqual(response.status_code, 200)

    def test_story_detail_view(self) -> None:
        client = Client()
        response = client.get(reverse("stories:story_detail", args=[self.story.slug]))
        self.assertEqual(response.status_code, 200)
