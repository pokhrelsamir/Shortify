from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ShortURLForm
from .models import ShortURL
from django.db.models import Q, Sum
from django.core.paginator import Paginator


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
    links = ShortURL.objects.all().order_by("-created_at")

    search_query = request.GET.get("q", "").strip()

    if search_query:
        links = links.filter(
            Q(original_url__icontains=search_query)
            | Q(short_code__icontains=search_query)
        )

    total_links = ShortURL.objects.count()

    total_clicks = ShortURL.objects.aggregate(
        total=Sum("clicks")
    )["total"] or 0

    average_clicks = (
        round(total_clicks / total_links, 1)
        if total_links
        else 0
    )

    paginator = Paginator(links, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "links": page_obj,
        "page_obj": page_obj,
        "search_query": search_query,
        "total_links": total_links,
        "total_clicks": total_clicks,
        "average_clicks": average_clicks,
    }

    return render(
        request,
        "links/dashboard.html",
        context
    )


def detail(request, short_code):
    link = get_object_or_404(
        ShortURL,
        short_code=short_code,
    )

    return render(
        request,
        "links/detail.html",
        {
            "link": link,
        },
    )


def delete_link(request, short_code):
    link = get_object_or_404(
        ShortURL,
        short_code=short_code,
    )

    if request.method == "POST":
        link.delete()

    return redirect("links:dashboard")