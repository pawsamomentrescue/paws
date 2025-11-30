from __future__ import annotations

from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("how-adoption-works/", views.how_adoption_works, name="how_adoption_works"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("sitemap/", views.sitemap, name="sitemap"),
]
