from __future__ import annotations

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Story


def story_list(request):
    stories = Story.objects.filter(is_published=True)

    story_type = request.GET.get("type") or ""
    q = request.GET.get("q") or ""

    if story_type:
        stories = stories.filter(type=story_type)
    if q:
        stories = stories.filter(Q(title__icontains=q) | Q(body__icontains=q))

    stories = stories.order_by("-published_at", "-created_at")

    paginator = Paginator(stories, 10)
    page_number = request.GET.get("page") or 1
    try:
        page_obj = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = paginator.page(1)

    context = {
        "stories": page_obj,
        "page_obj": page_obj,
        "paginator": paginator,
        "type": story_type,
        "q": q,
    }
    return render(request, "stories/story_list.html", context)


def story_detail(request, slug: str):
    story = get_object_or_404(Story, slug=slug, is_published=True)
    return render(request, "stories/story_detail.html", {"story": story})
