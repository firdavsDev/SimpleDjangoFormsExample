from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import AddressFormSet, CheckAnswerForm, ContactFormModel, SearchForm

# # HTML form example
# def contact_form_html(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         email = request.POST.get("email")
#         message = request.POST.get("message")

#         # Save the data to the database
#         Contact.objects.create(name=name, email=email, phone=phone, message=message)
#         messages.success(request, "Your message has been sent successfully.")
#         return redirect("contact:contact_form")

#     return render(request, "contact.html")


# # Form class example
# def contact_form_class(request):
#     if request.method == "POST":
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             # call save method
#             form.save()
#             messages.success(request, "Your message has been sent successfully.")
#             return redirect("contact:contact_form")
#         context = {"form": form}
#         return render(request, "contact.html", context)
#     # Get request
#     form = ContactForm()
#     context = {"form": form}
#     return render(request, "contact.html", context)


# ModelForm class example
def contact_form_model_class(request):
    search_form = SearchForm()
    form = ContactFormModel()
    if request.method == "POST":
        form = ContactFormModel(data=request.POST)
        if form.is_valid():
            instance = form.save()
            verification_code = instance.verification_code
            messages.success(
                request,
                f"Your message has been sent successfully. Your message verification code: {verification_code}",
            )
            return redirect("contact:contact_form")
    # Get request
    context = {"form": form, "search_form": search_form}
    return render(request, "contact.html", context)


def check_answer(request):
    if request.method == "POST":
        form = CheckAnswerForm(data=request.POST)
        if form.is_valid():
            # call save method
            answer = form.save()
            context = {"answer_form": form, "answer": answer}
            return render(request, "checkanswer.html", context)
        context = {"answer_form": form}
        return render(request, "checkanswer.html", context)
    # Get request
    form = CheckAnswerForm()
    context = {"answer_form": form}
    return render(request, "checkanswer.html", context)


def contact_inline_formset(request):
    if request.method == "POST":
        contact_form = ContactFormModel(request.POST)
        address_formset = AddressFormSet(request.POST)

        if contact_form.is_valid() and address_formset.is_valid():
            # Save Contact first
            contact = contact_form.save()

            # Process the Address forms
            for form in address_formset:
                if form.cleaned_data and not form.cleaned_data.get("DELETE", False):
                    address = form.save(commit=False)
                    address.contact = contact
                    address.save()

            # Redirect or display success message
            messages.success(request, "Your message has been sent successfully.")
            return redirect("contact:address_form")  # Replace with your success URL

    else:
        contact_form = ContactFormModel()
        address_formset = AddressFormSet()

    return render(
        request,
        "contact_formset.html",
        {
            "contact_form": contact_form,
            "address_formset": address_formset,
        },
    )
