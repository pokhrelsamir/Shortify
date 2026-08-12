from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ShortURLForm
from .models import ShortURL


def home(request):
    short_url = None

    if request.method == "POST":
        form = ShortURLForm(request.POST)

        if form.is_valid():
            short_url = form.save()
    else:
        form = ShortURLForm()

    context = {
        "form": form,
        "short_url": short_url,
    }

    return render(
        request,
        "links/home.html",
        context,
    )


def redirect_short_url(request, short_code):
    link = get_object_or_404(
        ShortURL,
        short_code=short_code,
    )

    link.clicks += 1
    link.save(update_fields=["clicks", "updated_at"])

    return redirect(link.original_url)


def dashboard(request):
    search_query = request.GET.get("q", "").strip()

    links = ShortURL.objects.all()

    if search_query:
        links = links.filter(
            Q(original_url__icontains=search_query)
            | Q(short_code__icontains=search_query)
        )

    total_links = ShortURL.objects.count()

    total_clicks = sum(
        link.clicks
        for link in ShortURL.objects.all()
    )

    context = {
        "links": links,
        "total_links": total_links,
        "total_clicks": total_clicks,
        "search_query": search_query,
    }

    return render(
        request,
        "links/dashboard.html",
        context,
    )


def detail(request, short_code):
    link = get_object_or_404(
        ShortURL,
        short_code=short_code,
    )

    return render(
        request,
        "links/detail.html",
        {"link": link},
    )


def delete_link(request, short_code):
    link = get_object_or_404(
        ShortURL,
        short_code=short_code,
    )

    if request.method == "POST":
        link.delete()

    return redirect("links:dashboard")