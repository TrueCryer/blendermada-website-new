from django.contrib import admin

from .models import AddOn


@admin.register(AddOn)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('version', 'actual', 'hidden')
