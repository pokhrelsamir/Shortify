from django.urls import path

from . import views


app_name = "links"


urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard",
    ),

    path(
        "link/<str:short_code>/",
        views.detail,
        name="detail",
    ),

    path(
        "link/<str:short_code>/delete/",
        views.delete_link,
        name="delete_link",
    ),

    path(
        "<str:short_code>/",
        views.redirect_short_url,
        name="redirect_short_url",
    ),
]