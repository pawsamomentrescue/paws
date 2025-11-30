from __future__ import annotations

from django.db import models


class Donation(models.Model):
    STATUS_PENDING = "pending"
    STATUS_SUCCEEDED = "succeeded"
    STATUS_FAILED = "failed"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_SUCCEEDED, "Succeeded"),
        (STATUS_FAILED, "Failed"),
    ]

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    message = models.TextField(blank=True)
    is_recurring = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"Donation from {self.full_name} ({self.amount})"
