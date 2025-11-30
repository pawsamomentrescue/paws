from __future__ import annotations

from django.urls import path

from . import views

app_name = "adoptions"

urlpatterns = [
    path("", views.animal_list, name="animal_list"),
    path("<slug:slug>/", views.animal_detail, name="animal_detail"),
    path("<slug:slug>/apply/", views.apply_for_animal, name="apply"),
    path("<slug:slug>/thanks/", views.application_thanks, name="application_thanks"),
]
