from django.shortcuts import render

from .forms import ShortURLForm


def home(request):
    short_url = None

    if request.method == "POST":
        form = ShortURLForm(request.POST)

        if form.is_valid():
            link = form.save()
            short_url = link
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