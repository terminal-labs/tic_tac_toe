from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.index', name='index'),                   
    url(r'^index/', 'app.views.index', name='index'),
    url(r'^game_board/', 'app.views.game_board', name='game_board'),                    
    url(r'^game_engine/', 'app.views.game_engine', name='game_engine'),                   
    url(r'^admin/', include(admin.site.urls)),
)

