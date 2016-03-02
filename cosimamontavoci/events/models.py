from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES= (
        ('draft','Draft'),
        ('published','Published'),
    )
    title=models.CharField(max_length=250)
    slug=models.CharField(max_length=250, unique_for_date='publish')
    author=models.ForeignKey(User, related_name='blog_posts')
    body=models.TextField(default=None)
    excerpt=models.TextField(default=None)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    photo=models.ImageField(upload_to='photos/',blank=True,null=True)
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
        return reverse('events:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug,
                             ])