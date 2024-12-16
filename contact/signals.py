from django.db.models.signals import post_save
from django.dispatch import receiver

import random

from .models import Contact


@receiver(post_save, sender=Contact)
def create_verification_code(sender, instance, created, **kwargs):
    if created:
        verification_code = ''
        list1 = ['1','2','3','4','5','a','b','c','d','e']

        for i in range(5):
            verification_code += random.choice(list1)

        instance.verification_code = verification_code
        instance.save()