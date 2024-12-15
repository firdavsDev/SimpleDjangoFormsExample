from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Include the contact app's URLs
    path("", include("contact.urls")),
]
