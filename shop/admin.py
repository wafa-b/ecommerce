from django.contrib import admin
from .models import Category, Product

# Register your models here.

admin.site.site_headre = 'Flowers Online Shop Adminstration'
admin.site.site_title = 'Flowers Online Shop Adminstration'

# @admin.register(Category)
class  CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['name']
    list_display = ['name',]
    list_filter = ['created_at']
    prepopulated_fields = {'slug':('name',)}




class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['name']
    list_display = ['name', 'price', 'stock', 'category',]
    list_filter = ['created_at', 'category',]
    prepopulated_fields = {'slug':('name',)}
    actions = ['discount',]


    # def discount(self, request, queryset):
    #     for product in queryset:
    #         product.price = product.price * decimal.Decimal('0.8')
    #         product.save()
    # discount.short_description = 'Apply 20%% DISCOUNT'

admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)

