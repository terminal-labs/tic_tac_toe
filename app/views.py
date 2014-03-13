import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Context
from django.template.loader import get_template

from game_logic_core import next_game_state

def index(request):
    # I need to rework this view to be a more pleasant homepage.
    t = get_template('base.html')
    html = t.render(Context())
    return HttpResponse(html)

def game_board(request):
    t = get_template('base.html')
    html = t.render(Context())
    return HttpResponse(html)

def game_engine(request):
    if request.method == 'GET':
        json_string = request.GET.get('json_string')
        
        # Make sure that the 'json_string' arg is in the reguest.
        if json_string is None:
            return HttpResponseBadRequest()

        game_state = json.loads(json_string)
        
        game_dict = next_game_state(game_state)

        return HttpResponse(json.dumps(game_dict))
