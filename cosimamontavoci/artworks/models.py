from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Artwork(models.Model):
    STATUS_CHOICES= (
        ('draft','Draft'),
        ('published','Published'),
    )
    title=models.CharField(max_length=250)
    slug=models.CharField(max_length=250, unique_for_date='publish')
    seo_description=models.TextField(null=True, blank=True)
    author=models.ForeignKey(User, related_name='artwork_posts')
    body=models.TextField(default=None)
    year=models.CharField(max_length=4, null=True, blank=True)
    materials=models.CharField(max_length=500, null=True, blank=True)
    measures=models.CharField(max_length=500, null=True, blank=True)
    exhibited=models.TextField(null=True, blank=True)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    objects= models.Manager()
    published=PublishedManager()

    class Meta:
        ordering= ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('artworks:artwork_detail',
                       args=[
                             self.slug,
                             ])


class ArtworkImage(models.Model):
    name = models.ForeignKey(Artwork, related_name='images')
    image = models.ImageField(upload_to='photos/')
    order=models.IntegerField()

    class Meta:
        ordering=('order',)