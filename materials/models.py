from pathlib import Path
from uuid import uuid4

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from sorl.thumbnail import ImageField

from users.models import User


def get_uuid_filename(filename):
    name = uuid4()
    ext = Path(filename).suffix
    return f"{name}{ext}"


def get_image_filename(instance, filename):
    return Path('materials', 'images', get_uuid_filename(filename))


def get_storage_filename(instance, filename):
    return Path('materials', 'storages', get_uuid_filename(filename))


class Category(models.Model):

    name = models.CharField(_('name'), max_length=25)
    slug = models.SlugField(_('slug'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ['name']

    def __str__(self):
        return self.name


class MaterialManager(models.Manager):

    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(draft=False, **kwargs)


class Material(models.Model):

    ENGINES = (
        ('cyc', 'Cycles'),
        ('eve', 'Eevee'),
        ('lux', 'Lux Render'),
        ('yfr', 'YafaRay'),
        ('oct', 'Octane'),
        ('nox', 'NOX Render'),
        ('int', 'Blender Internal'),
    )

    engine = models.CharField(
        _('render engine'), max_length=3, choices=ENGINES)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='materials',
        blank=True, null=True,
    )
    name = models.CharField(_('name'), max_length=20)
    slug = models.SlugField(_('slug'))
    description = models.TextField(_('description'), blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='materials',
        blank=True, null=True,
    )
    date = models.DateTimeField(_('date'), auto_now_add=True)
    draft = models.BooleanField(_('draft'), default=True)
    storage = models.FileField(
        _('storage'), upload_to=get_storage_filename, blank=True
    )
    storage_name = models.CharField(_('storage name'), max_length=50)
    preview = ImageField(
        _('preview'), upload_to=get_image_filename, blank=True
    )
    downloads = models.IntegerField(_('number of downloads'), default=0)
    rating = models.FloatField(_('rating'), default=0)
    votes_count = models.IntegerField(_('number of votes'), default=0)

    objects = MaterialManager()

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('materials:detail', kwargs={
            'pk': self.pk,
            'slug': self.slug,
        })


class Vote(models.Model):

    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='votes',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='votes',
        blank=True, null=True,
    )
    score = models.PositiveIntegerField(_('score'))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('vote')
        verbose_name_plural = _('votes')
        ordering = ['-modified_at']
        unique_together = ('material', 'user')

    def __str__(self):
        return f"{self.user} - {self.material}"
