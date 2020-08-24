from django.contrib import admin
from .models import *

admin.site.register(BodyShape)
admin.site.register(Manufacturer)
admin.site.register(WireType)


@admin.register(FeedbackForm)
class FeedbackFormAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(BillingForm)
class BillingFormAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
