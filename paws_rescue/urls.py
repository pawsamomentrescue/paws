from __future__ import annotations

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("adopt/", include("adoptions.urls")),
    path("stories/", include("stories.urls")),
    path("donate/", include("donations.urls")),
]
