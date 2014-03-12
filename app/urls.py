from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	# Regex for website root.
    url(r'^$', 'app.views.index', name='index'),
    
    # Show the gameboard and load the JS components in the browser.
    url(r'^game_board/', 'app.views.game_board', name='game_board'),
    
    # Send AJAX requests to the view that handles gameplay interactions.
    url(r'^game_engine/', 'app.views.game_engine', name='game_engine'),
    
    # Django admin, overkill for a Tic Tac Toe game?
    url(r'^admin/', include(admin.site.urls)),
)
