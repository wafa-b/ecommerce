from django.contrib import admin
from .models import Coupons


# Register your models here.

class CouponsAdmin(admin.ModelAdmin):
    list_display = ('code','valid_form','valid_to','discount','active',)
    list_filter = ('active','valid_form','valid_to',)
    search_fields = ('code',)

admin.site.register(Coupons, CouponsAdmin)
