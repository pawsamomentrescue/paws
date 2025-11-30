from __future__ import annotations

from django.contrib import admin

from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "is_published", "published_at")
    list_filter = ("type", "is_published")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
