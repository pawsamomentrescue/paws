from __future__ import annotations

from django.urls import path

from . import views

app_name = "stories"

urlpatterns = [
    path("", views.story_list, name="story_list"),
    path("<slug:slug>/", views.story_detail, name="story_detail"),
]
