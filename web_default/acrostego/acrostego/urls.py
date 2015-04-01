from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'acrostego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^frontend/', include('frontend.urls')),
    url(r'^$', include('frontend.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
