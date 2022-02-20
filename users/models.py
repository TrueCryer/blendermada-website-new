from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):

    # About
    about = models.TextField(_('about'), blank=True)

    # Settings
    send_newsletters = models.BooleanField(
        _('send newsletters'),
        default=False,
    )
    send_notifications = models.BooleanField(
        _('send notifications'),
        default=False,
    )
    show_fullname = models.BooleanField(
        _('show full name'),
        default=False,
    )
    show_email = models.BooleanField(
        _('show e-mail'),
        default=False,
    )

    # Socials
    website = models.CharField(_('website'), max_length=255, blank=True)
    deviantart = models.CharField(_('deviantart'), max_length=255, blank=True)
    facebook = models.CharField(_('facebook'), max_length=255, blank=True)
    twitter = models.CharField(_('twitter'), max_length=255, blank=True)
