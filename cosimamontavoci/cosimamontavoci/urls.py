from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from events.sitemaps import PostSitemap
from artworks.sitemaps import ArtworkSitemap
from glass.sitemaps import GlassSitemap

admin.autodiscover()

sitemaps = {
    'posts': PostSitemap,
    'artworks': ArtworkSitemap,
    'glass': GlassSitemap,
}

urlpatterns = patterns('',
    url(r'^$', 'views.home' , name='home'),
    url(r'^events/', include('events.urls',namespace='events',app_name='events')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^artworks/', include('artworks.urls',namespace='artworks', app_name='artworks')),
    url(r'^about/', 'views.about', name='about'),
    url(r'^lampwork-jewelry/', include('glass.urls', namespace='glass', app_name='glass')),
    url(r'^contact/$', 'contact.views.contact_form', name='contact_form'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
)

urlpatterns+= staticfiles_urlpatterns()

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)