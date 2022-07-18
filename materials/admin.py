from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Category, Material, Vote


def make_thumbs(modeladmin, request, queryset):
    for obj in queryset:
        obj.make_thumbs()
make_thumbs.short_description = _("Make thumbs to selected")


class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(Material)
class MaterialAdmin(SlugAdmin):
    list_display = (
        'name', 'pk', 'category', 'engine', 'author', 'date',
        'storage_name', 'downloads'
    )
    list_filter = ('engine', 'category')
    list_per_page = 25
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': (
                ('name', 'slug'),
                'description',
                ('engine', 'category'),
                ('user')
            )
        }),
        (_('Publish'), {
            'classes': ('collapse',),
            'fields': ('draft', 'downloads')
        }),
        (_('Files'), {
            'classes': ('collapse',),
            'fields': (
                'preview',
                'storage', 'storage_name'
            ),
        }),
    )
    readonly_fields = ('downloads',)
    actions = [make_thumbs]


@admin.register(Category)
class CategoryAdmin(SlugAdmin):
    pass


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
