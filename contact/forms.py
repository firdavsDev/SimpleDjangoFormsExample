from django import forms

from .models import Contact, Region


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Search here..."}),
    )


# Form class example
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100
        # widget=forms.TextInput(attrs={"type": "number"})
    )
    email = forms.EmailField(required=False)
    phone = forms.CharField(
        max_length=15,
        # help_text="Phone number must start with +998 and have 13 digits.",
        label="Phone",
    )
    message = forms.CharField(widget=forms.Textarea)
    jins = forms.ChoiceField(
        choices=[("erkak", "Erkak"), ("ayol", "Ayol")], widget=forms.RadioSelect
    )

    # validate phone number (clean_field_name)
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.startswith("+998") or len(phone) != 13:
            raise forms.ValidationError(
                "Phone number must start with +998 and have 13 digits."
            )
        return phone

    # save data to the database
    def save(self):
        name = self.cleaned_data["name"]
        phone = self.cleaned_data["phone"]
        email = self.cleaned_data["email"]
        message = self.cleaned_data["message"]

        # Save the data to the database
        contact_obj = Contact.objects.create(
            name=name, email=email, phone=phone, message=message
        )
        return contact_obj


class ContactFormModel(forms.ModelForm):
    jins = forms.ChoiceField(
        choices=[("erkak", "Erkak"), ("ayol", "Ayol")], widget=forms.RadioSelect
    )
    region = forms.ModelChoiceField(
        queryset=Region.objects.filter(is_active=True),
        empty_label="Select region",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    # def clean(self):
    #     # for validation of all fields
    #     return super().clean()

    # valifdate (clean_field_name)
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.startswith("+998") or len(phone) != 13:
            raise forms.ValidationError(
                "Phone number must start with +998 and have 13 digits."
            )
        return phone

    class Meta:
        model = Contact
        # fields = ("name", "email", "phone", "message")
        exclude = ["is_answered"]
        labels = {
            "name": "Your Name",
            "email": "Your Email",
            "phone": "Your Phone",
            "message": "Your Message",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your name"}
            ),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }
        error_css_class = "danger"

        # help_texts = {
        #     "phone": "Phone number must start with +998 and have 13 digits.",
        # }
        # error_messages = {
        #     "name": {
        #         "required": "Name field is required.",
        #         "max_length": "Name field must be less than 100 characters.",
        #     },
        #     "phone": {
        #         "required": "Phone field is required.",
        #         "max_length": "Phone field must be less than 15 characters.",
        #     },
        #     "message": {
        #         "required": "Message field is required.",
        #     },
        # }

        # field_classes = {
        #     "name": forms.CharField,
        #     "email": forms.EmailField,
        #     "phone": forms.CharField,
        #     "message": forms.CharField,
        # }
        # localized_fields = "__all__"
        # required_css_class = "required"