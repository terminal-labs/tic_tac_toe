import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Context
from django.template.loader import get_template

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

        request_game_state = json.loads(json_string)
        response_game_state = request_game_state
        
        game_over_flag = 0
        cells_remaining = response_game_state.count(' ')
        if cells_remaining > 1:
			# Select the first available cell and change it to 'o'. Does not guarantee computer win or draw yet.
            index = response_game_state.index(' ')
            response_game_state[index] = 'o'
        elif cells_remaining == 0:
			# The game must be over if all the cells are marked.
            game_over_flag = 1
        
        game_winner = 'none' # Winner determination logic not implemented yet.
        
        reponse_dict = {'game_winner': game_winner,'game_over_flag': game_over_flag, 'game_state': response_game_state}

        return HttpResponse(json.dumps(reponse_dict))
