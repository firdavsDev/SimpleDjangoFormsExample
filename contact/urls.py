from django.urls import path

from . import views

# app_name is used to help Django distinguish between URLs with the same name
app_name = "contact"

urlpatterns = [
    # path("", views.contact_form_class, name="contact_form"),
    path("", views.contact_form_model_class, name="contact_form"),
    path("answer/", views.check_answer, name="check_answer"),
]
