from game_logic_core import next_game_state

def test_match(play_order):
    game_state = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    for test in play_order:

        cell_index = 0
        choice_list = []

        for cell in game_state:
            if cell == ' ':
                choice_list.append(cell_index)
            cell_index = cell_index + 1
             
        game_state[choice_list[test - 1]] = 'x'
        game_state_dict = next_game_state(game_state)
        if game_state_dict['game_over_flag'] == 1:
            return game_state_dict

test_games = []
for first_move in range(0, 9):
    for second_move in range(0, 8):
        for third_move in range(0, 5):
            for forth_move in range(0, 3):
                for fifth_move in range(0, 2):
                    test_games.append([first_move, second_move, third_move, forth_move, fifth_move, 0])

number_of_x_wins = 0
for possible_game in test_games:
    game_state_dict = test_match(possible_game)
    if game_state_dict['game_winner'] == 'x':
       number_of_x_wins = number_of_x_wins + 1

print number_of_x_wins
