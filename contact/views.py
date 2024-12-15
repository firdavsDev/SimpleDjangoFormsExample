from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm, ContactFormModel, SearchForm
from .models import Contact


# HTML form example
def contact_form_html(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save the data to the database
        Contact.objects.create(name=name, email=email, phone=phone, message=message)
        messages.success(request, "Your message has been sent successfully.")
        return redirect("contact:contact_form")

    return render(request, "contact.html")


# Form class example
def contact_form_class(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            # call save method
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect("contact:contact_form")
        context = {"form": form}
        return render(request, "contact.html", context)
    # Get request
    form = ContactForm()
    context = {"form": form}
    return render(request, "contact.html", context)


# ModelForm class example
def contact_form_model_class(request):
    search_form = SearchForm()
    if request.method == "POST":
        form = ContactFormModel(data=request.POST)
        if form.is_valid():
            # call save method
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect("contact:contact_form")
        context = {"form": form, "search_form": search_form}
        return render(request, "contact.html", context)
    # Get request
    form = ContactFormModel()
    context = {"form": form, "search_form": search_form}
    return render(request, "contact.html", context)
