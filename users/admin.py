from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class ExtendedUserAdmin(UserAdmin):
    fieldsets = (
        (
            None, {
                "fields": ("username", "password")
            }
        ),
        (
            _("Personal info"), {
                "fields": ("first_name", "last_name", "email", "about")
            }
        ),
        (
            _("Settings"), {
                "fields": (
                    "send_newsletters",
                    "send_notifications",
                    "show_fullname",
                    "show_email",
                )
            }
        ),
        (
            _("Social"), {
                "fields": ("website", "deviantart", "facebook", "twitter")
            }
        ),
        (
            _("Permissions"), {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
