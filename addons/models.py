from pathlib import Path

from django.db import models
from django.utils.translation import gettext as _


def get_addon_path(instance, filename):
    return Path('addons', instance.version, filename)


class AddOnManager(models.Manager):

    def actual(self, **kwargs):
        return self.filter(actual=True, **kwargs)

    def published(self, **kwargs):
        return self.filter(hidden=False, **kwargs)


class AddOn(models.Model):

    version = models.CharField(_('version'), max_length=10)
    changelog = models.TextField(_('changelog'), blank=True)

    actual = models.BooleanField(_('actual'))
    hidden = models.BooleanField(_('hidden'))

    storage = models.FileField(_('storage'), upload_to=get_addon_path)

    objects = AddOnManager()

    class Meta:
        verbose_name = 'Add-on'
        verbose_name_plural = 'Add-ons'
        ordering = ['-version']

    def __str__(self):
        return f'{self.version}'
