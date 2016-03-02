from django.conf.urls import url, patterns
from . import views


urlpatterns= patterns(
    'glass.views',
    url(r'^$', views.glass_list, name='glass_list'),
    url(r'^(?P<glass_item>[-\w]+)/$', views.glass_detail , name='glass_detail'),
)