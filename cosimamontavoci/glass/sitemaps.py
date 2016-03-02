from django.contrib.sitemaps import Sitemap
from .models import Glass

class GlassSitemap(Sitemap):
    changefreq='weekly'
    priority=0.9

    def items(self):
        return Glass.published.all()

    def lastmod(self,obj):
        return obj.publish