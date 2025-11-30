from __future__ import annotations

from django import forms

from .models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["full_name", "email", "amount", "message", "is_recurring"]
