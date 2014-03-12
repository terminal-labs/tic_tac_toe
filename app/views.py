import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Context
from django.template.loader import get_template

def all_same(*args):
    if len(set(args)) == 1:
        return True
    return False

def did_player_win(game_state, player):
    gs = game_state

    for row in [0,3,6]:
        if all_same(gs[row], gs[row + 1], gs[row + 2], player):
            return True

    for col in [0,1,2]:
        if all_same(gs[col], gs[col + 3], gs[col + 6], player):
            return True

    if all_same(gs[0],gs[4],gs[8],player):
        return True

    if all_same(gs[2], gs[4], gs[6], player):
        return True
    
    return False

def who_won(game_state):
    if did_player_win(game_state, 'x') == True:
        return 'x'
    elif did_player_win(game_state, 'o') == True:
        return 'o'

def try_win(game_state):
    gs = game_state

    # Check for 2 out of 3 'x's in rows.
    for row in [0,3,6]:
        row_list = [gs[row], gs[row + 1], gs[row + 2]]
        if row_list.count('o') == 2 and row_list.count(' ') == 1:
            move_index = row_list.index(' ')
            game_state[row + move_index] = 'o'
            return True

    # Check for 2 out of 3 'x's in cols.     
    for col in [0,1,2]:
        col_list = [gs[col], gs[col + 3], gs[col + 6]]
        if col_list.count('o') == 2 and col_list.count(' ') == 1:
            move_index = col_list.index(' ')
            game_state[col + move_index*3] = 'o'
            return True

    # Check for 2 out of 3 'x's in top left to lower right diagonal.                                                                                   
    diagonal_list = [gs[0],gs[4],gs[8]]
    if diagonal_list.count('o') == 2 and diagonal_list.count(' ') == 1:
        move_index = diagonal_list.index(' ')
        game_state[move_index*4] = 'o'
        return True

    # Check for 2 out of 3 'x'' in lower left to top right diagonal.                                                                                       
    diagonal_list = [gs[2],gs[4],gs[6]]
    if diagonal_list.count('o') == 2 and diagonal_list.count(' ') == 1:
        move_index = diagonal_list.index(' ')
        game_state[move_index*2 + 2] = 'o'
        return True

    return False

def try_block(game_state):
    gs = game_state

    # Check for 2 out of 3 'x's in rows.
    for row in [0,3,6]:
        row_list = [gs[row], gs[row + 1], gs[row + 2]]
        if row_list.count('x') == 2 and row_list.count(' ') == 1:
            move_index = row_list.index(u' ')
            game_state[row + move_index] = 'o'
            return True

    # Check for 2 out of 3 'x's in cols.    
    for col in [0,1,2]:
        col_list = [gs[col], gs[col + 3], gs[col + 6]]
        if col_list.count('x') == 2 and col_list.count(' ') == 1:
            move_index = col_list.index(' ')
            game_state[col + move_index*3] = 'o'
            return True

    # Check for 2 out of 3 'x's in top left to lower right diagonal.    
    diagonal_list = [gs[0],gs[4],gs[8]]     
    if diagonal_list.count('x') == 2 and diagonal_list.count(' ') == 1:
        move_index = diagonal_list.index(' ')
        game_state[move_index*4] = 'o'
        return True

    # Check for 2 out of 3 'x'' in lower left to top right diagonal.     
    diagonal_list = [gs[2],gs[4],gs[6]]
    if diagonal_list.count('x') == 2 and diagonal_list.count(' ') == 1:
        move_index = diagonal_list.index(' ')
        game_state[move_index*2 + 2] = 'o'
        return True
        
    return False

def try_center(game_state):
    gs = game_state
    if gs[4] == ' ':
        gs[4] = 'o'
        return True
    return False

def try_empty_corner(game_state):
    gs = game_state
    for cell_index in [0,2,6,8]:
        if gs[cell_index] == ' ':
            gs[cell_index] = 'o'
            return True
    return False
    
def is_game_over(game_state):
    if game_state.count(' ') == 0:
        return True
    elif did_player_win(game_state, 'x') == True:
        return True
    elif did_player_win(game_state, 'o') == True:
        return True

    return False

def make_move(game_state):
    gs = game_state
    if try_win(gs):
        return
    elif try_block(gs):
        return
    #elif try_fork(gs):
    #    return
    #elif try_fork_block(gs):
    #    return
    elif try_center(gs):
        return
    #elif try_opposite_corner(gs):
    #    return
    elif try_empty_corner(gs):
        return
    #elif try_emtpy_side(gs):
    #    return

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

        if is_game_over(game_state) == False:
            game_over_flag = 0
            # Since no one has won yet, it is the computers move.
            cells_remaining = game_state.count(' ')
            
            if cells_remaining > 0:
                make_move(game_state) 

            if is_game_over(game_state) == True: 
                game_over_flag = 1
        else:
            game_over_flag = 1
        
        game_winner = False
        if game_over_flag == 1:
            game_winner = who_won(game_state)
        reponse_dict = {'game_winner': game_winner,'game_over_flag': game_over_flag, 'game_state': game_state}

        return HttpResponse(json.dumps(reponse_dict))
