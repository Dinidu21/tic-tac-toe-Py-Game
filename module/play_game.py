from board import sign_dict, print_board, reset_game

def take_input(player_name):
    while True:
        x = input(f'{player_name}: ')
        if x.lower() == '#':
            return 'exit'
        try:
            x = int(x) - 1
            if 0 <= x < 9:
                if sign_dict[x] != ' ':
                    print('This spot is already taken. Please choose another spot.')
                    continue
                return x
            else:
                print('Invalid input. Please enter a number between 1 and 9.')
        except ValueError:
            print('Invalid input. Please enter a number or "exit" to quit the game.')

def result_calculation(player_one, player_two):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for combo in winning_combinations:
        if sign_dict[combo[0]] == sign_dict[combo[1]] == sign_dict[combo[2]] != ' ':
            winner = player_one if sign_dict[combo[0]] == 'X' else player_two
            return winner
    return None
