from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("links.urls")),
]

handler404 = "links.views.custom_404"
handler500 = "links.views.custom_500"