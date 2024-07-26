# Instructions for the game
instructions = """
This will be our Tic Tac Toe board...
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

*I N S T R U C T I O N S:
1. Insert the spot number(1-9) to put your sign
2. Player 1 will go first.
3. If you want to exit the game, enter #
"""

# Initialize the board with blank spots
sign_dict = [' ' for _ in range(9)]

def print_board(sign_dict):
    board = f"""
   {sign_dict[0]} | {sign_dict[1]} | {sign_dict[2]}
  ---|---|---
   {sign_dict[3]} | {sign_dict[4]} | {sign_dict[5]}
  ---|---|---
   {sign_dict[6]} | {sign_dict[7]} | {sign_dict[8]}
  """
    print(board)

def reset_game():
    for i in range(9):
        sign_dict[i] = ' '
