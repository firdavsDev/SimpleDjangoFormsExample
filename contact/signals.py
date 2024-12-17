from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Contact
from .utils import genereate_code


@receiver(post_save, sender=Contact)
def create_verification_code(sender, instance, created, **kwargs):
    if created:
        # Generate a verification code
        code = genereate_code()

        instance.verification_code = code
        instance.save()
