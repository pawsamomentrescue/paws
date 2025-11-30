from __future__ import annotations

from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import DonationForm
from .payment import payment_provider


def donate(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            result = payment_provider.charge(amount=donation.amount, description=f"Donation from {donation.full_name}")
            donation.status = donation.STATUS_SUCCEEDED if result.success else donation.STATUS_FAILED
            donation.save()
            return redirect(reverse("donations:thanks"))
    else:
        form = DonationForm()
    return render(request, "donations/donation_form.html", {"form": form})


def thanks(request):
    return render(request, "donations/donation_thanks.html")
