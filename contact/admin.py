from django.contrib import admin

from .models import Contact, Region, ContactAnswer

# TODO chiroyli qil
admin.site.register(Contact)
admin.site.register(Region)
admin.site.register(ContactAnswer)
