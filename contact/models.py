from django.core.exceptions import ValidationError
from django.db import models


def phone_validator(value):
    # check phone start +998 and length 13
    if not value.startswith("+998") or len(value) != 13:
        raise ValidationError("Phone number must start with +998 and have 13 digits.")
    return value


class Region(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class Contact(models.Model):
    # code = models.CharField(max_length=10, unique=True)

    name = models.CharField(max_length=100, verbose_name="Full name")
    phone = models.CharField(
        max_length=15, validators=[phone_validator], verbose_name="Phone number"
    )
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    verification_code = models.CharField(
        max_length=5, verbose_name="verification_code", null=True
    )
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Address(models.Model):
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name="addresses"
    )
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    district = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.region} - {self.district} - {self.street} - {self.house}"

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class ContactAnswer(models.Model):
    contact = models.OneToOneField(
        Contact, on_delete=models.CASCADE, verbose_name="answer"
    )
    answer = models.TextField()

    def __str__(self):
        return self.contact.name

    def save(self, *args, **kwargs):
        self.contact.is_answered = True
        self.contact.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Contact Answer"
        verbose_name_plural = "Contact Answers"
