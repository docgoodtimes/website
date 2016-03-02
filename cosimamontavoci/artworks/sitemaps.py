from django.contrib.sitemaps import Sitemap
from .models import Artwork

class ArtworkSitemap(Sitemap):
    changefreq='weekly'
    priority=0.9

    def items(self):
        return Artwork.published.all()

    def lastmod(self,obj):
        return obj.publish