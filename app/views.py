import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Context
from django.template.loader import get_template

def index(request):
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
        if json_string is None:
            return HttpResponseBadRequest()

        request_game_state = json.loads(json_string)        
        response_game_state = request_game_state
        
        game_over_flag = 0
        cells_remaining = response_game_state.count(' ')
        if cells_remaining > 1:
            index = response_game_state.index(' ')
            response_game_state[index] = 'o'
        elif cells_remaining == 0:
            game_over_flag = 1
        
        game_winner = 'none'
        reponse_dict = {'game_winner': game_winner,'game_over_flag': game_over_flag, 'game_state': response_game_state}

        return HttpResponse(json.dumps(reponse_dict))
