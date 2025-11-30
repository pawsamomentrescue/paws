from __future__ import annotations

from django.db import models

from adoptions.models import Animal


class Story(models.Model):
    TYPE_NEWS = "news"
    TYPE_SUCCESS = "success"

    TYPE_CHOICES = [
        (TYPE_NEWS, "News"),
        (TYPE_SUCCESS, "Success Story"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TYPE_NEWS)
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    related_animal = models.ForeignKey(Animal, null=True, blank=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.title
