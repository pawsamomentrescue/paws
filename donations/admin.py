from __future__ import annotations

from django.contrib import admin

from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "amount", "is_recurring", "status", "created_at")
    list_filter = ("status", "is_recurring", "created_at")
    search_fields = ("full_name", "email")
