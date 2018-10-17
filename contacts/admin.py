from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'listing', 'phone', 'message', 'contact_date')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'listing')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
