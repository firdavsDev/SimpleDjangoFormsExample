from django.contrib import admin

from .models import Address, Contact, ContactAnswer, Region

# TODO chiroyli qil
admin.site.register(Region)
admin.site.register(Address)


class ContactAnswerInline(admin.StackedInline):
    model = ContactAnswer


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", "is_answered"]
    list_filter = ["is_answered"]
    search_fields = ["name", "phone", "email"]
    list_editable = ["is_answered"]
    list_per_page = 10
    inlines = [ContactAnswerInline]


admin.site.register(Contact, ContactAdmin)
