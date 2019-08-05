from django.contrib import admin
from .models import ContactUs

# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    search_fields = ['name']
    list_display = ['name', 'subject', 'message','email','created_date',]
    list_filter = ['created_date', 'subject',]

admin.site.register(ContactUs, ContactUsAdmin)
