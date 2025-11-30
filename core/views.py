from __future__ import annotations

from django.shortcuts import render

from adoptions.models import Animal
from stories.models import Story


def home(request):
    featured_animals = Animal.objects.filter(status="available").order_by("-intake_date")[:3]
    recent_stories = Story.objects.filter(is_published=True).order_by("-published_at")[:3]
    return render(
        request,
        "core/home.html",
        {
            "featured_animals": featured_animals,
            "recent_stories": recent_stories,
        },
    )


def how_adoption_works(request):
    return render(request, "core/how_adoption_works.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")


def sitemap(request):
    return render(request, "core/sitemap.html")
