from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.index', name='index'),                   
    url(r'^index/', 'app.views.index', name='index'),
    url(r'^date/', 'app.views.date', name='date'),
    url(r'^admin/', include(admin.site.urls)),
)
