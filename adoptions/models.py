from __future__ import annotations

from django.db import models


class Animal(models.Model):
    STATUS_AVAILABLE = "available"
    STATUS_PENDING = "pending"
    STATUS_ADOPTED = "adopted"

    STATUS_CHOICES = [
        (STATUS_AVAILABLE, "Available"),
        (STATUS_PENDING, "Pending"),
        (STATUS_ADOPTED, "Adopted"),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100, blank=True)
    age_years = models.PositiveIntegerField(null=True, blank=True)
    size = models.CharField(max_length=20, blank=True)
    sex = models.CharField(max_length=10, blank=True)
    suburb = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_AVAILABLE)
    intake_date = models.DateField()
    photo_url = models.URLField(blank=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    adoption_fee = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    good_with_kids = models.BooleanField(default=False)
    special_needs = models.BooleanField(default=False)
    microchipped = models.BooleanField(default=False)
    vaccinated = models.BooleanField(default=False)
    desexed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name



class AnimalPhoto(models.Model):
    animal = models.ForeignKey(Animal, related_name="photos", on_delete=models.CASCADE)
    image_url = models.URLField()
    is_primary = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"Photo for {self.animal}"


class AdoptionApplication(models.Model):
    STATUS_NEW = "new"
    STATUS_REVIEWING = "reviewing"
    STATUS_APPROVED = "approved"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_NEW, "New"),
        (STATUS_REVIEWING, "Reviewing"),
        (STATUS_APPROVED, "Approved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    animal = models.ForeignKey(Animal, related_name="applications", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"Application for {self.animal} by {self.full_name}"
