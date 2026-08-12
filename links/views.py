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