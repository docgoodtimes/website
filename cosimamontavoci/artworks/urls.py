from django.conf.urls import url, patterns
from . import views


urlpatterns= patterns(
    'artworks.views',
    url(r'^$', views.artwork_list, name='artwork_list'),
    url(r'^(?P<artwork>[-\w]+)/$', views.artwork_detail , name='artwork_detail'),
)