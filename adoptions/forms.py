from __future__ import annotations

from django import forms

from .models import AdoptionApplication


class AdoptionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = [
            "full_name",
            "email",
            "phone",
            "address",
            "message",
        ]
