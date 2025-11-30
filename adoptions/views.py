from __future__ import annotations

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import AdoptionApplicationForm
from .models import Animal


def animal_list(request):
    animals = Animal.objects.filter(status=Animal.STATUS_AVAILABLE)

    species = request.GET.get("species") or ""
    size = request.GET.get("size") or ""
    q = request.GET.get("q") or ""

    if species:
        animals = animals.filter(species__iexact=species)
    if size:
        animals = animals.filter(size__iexact=size)
    if q:
        animals = animals.filter(
            Q(name__icontains=q) | Q(breed__icontains=q) | Q(description__icontains=q)
        )

    animals = animals.order_by("name")

    paginator = Paginator(animals, 10)
    page_number = request.GET.get("page") or 1
    try:
        page_obj = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = paginator.page(1)

    context = {
        "animals": page_obj,
        "page_obj": page_obj,
        "paginator": paginator,
        "species": species,
        "size": size,
        "q": q,
    }
    return render(request, "adoptions/animal_list.html", context)


def animal_detail(request, slug: str):
    animal = get_object_or_404(Animal, slug=slug)
    photos = list(animal.photos.all())
    primary_photo = None
    for p in photos:
        if p.is_primary:
            primary_photo = p
            break
    if primary_photo is None and photos:
        primary_photo = photos[0]
    return render(
        request,
        "adoptions/animal_detail.html",
        {"animal": animal, "photos": photos, "primary_photo": primary_photo},
    )


def apply_for_animal(request, slug: str):
    animal = get_object_or_404(Animal, slug=slug)
    if request.method == "POST":
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.animal = animal
            application.save()
            return redirect(reverse("adoptions:application_thanks", args=[animal.slug]))
    else:
        form = AdoptionApplicationForm()
    return render(request, "adoptions/apply.html", {"animal": animal, "form": form})


def application_thanks(request, slug: str):
    animal = get_object_or_404(Animal, slug=slug)
    return render(request, "adoptions/application_thanks.html", {"animal": animal})
