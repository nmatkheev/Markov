from django.conf.urls import patterns, url

from frontend import views

urlpatterns = patterns('',
    url(r'^acrstg/', views.acrstg, name='acrstg'),
    url(r'^$', views.index, name='index')
)
