from django.contrib import admin

# Register your models here.
from .models import Listing


class listingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','price','realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'price')
    list_editable = ('is_published',)
    search_fields = ('id', 'title', 'price', 'realtor')
    list_per_page = 25


admin.site.register(Listing, listingAdmin)


