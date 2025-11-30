from __future__ import annotations

from django.contrib import admin

from .models import AdoptionApplication, Animal, AnimalPhoto


class AnimalPhotoInline(admin.TabularInline):
    model = AnimalPhoto
    extra = 1


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "suburb", "status", "intake_date")
    list_filter = ("status", "species", "suburb")
    search_fields = ("name", "breed", "description", "suburb")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [AnimalPhotoInline]


@admin.register(AdoptionApplication)
class AdoptionApplicationAdmin(admin.ModelAdmin):
    list_display = ("animal", "full_name", "email", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("full_name", "email", "animal__name")
