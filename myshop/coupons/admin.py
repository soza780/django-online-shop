from django.contrib import admin
from .models import Coupon


# Register your models here.

@admin.register(Coupon)
class CouponModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount', 'valid_from', 'valid_to', ]
    list_filter = ['active', 'valid_from', 'valid_to', ]
    search_fields = ['code']
