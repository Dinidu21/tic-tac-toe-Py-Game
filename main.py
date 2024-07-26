import sys
import os

# Get the absolute path of the module directory
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'module'))
sys.path.append(module_path)

from board import instructions, sign_dict, print_board, reset_game
from play_game import take_input, result_calculation
from history import save_stats, view_history

def play_game(player_one, player_two):
    stats = {'player_one_wins': 0, 'player_two_wins': 0, 'draws': 0}
    rounds = []  # To store the result of each round

    while True:
        print(instructions)
        print(f"Mr./Mrs. {player_one}'s sign is - X")
        print(f"Mr./Mrs. {player_two}'s sign is - O")
        input("Enter any key to start the game: ")

        # Reset the board
        reset_game()
        print_board(sign_dict)

        for i in range(9):
            if i % 2 == 0:
                index = take_input(player_one)
                if index == 'exit':
                    return stats, rounds
                sign_dict[index] = 'X'
            else:
                index = take_input(player_two)
                if index == 'exit':
                    return stats, rounds
                sign_dict[index] = 'O'
            print_board(sign_dict)
            result = result_calculation(player_one, player_two)
            if result:
                rounds.append(result)
                if result == player_one:
                    stats['player_one_wins'] += 1
                else:
                    stats['player_two_wins'] += 1
                print(f"Congratulations {result}! You won!")
                break
        else:
            print("This is a tie..!! Nobody won.")
            rounds.append('draw')
            stats['draws'] += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThank you both for playing!")
            break
    return stats, rounds

def welcome_page():
    welcome = "Welcome to Tic Tac Toe game"
    print(welcome.center(40, "\\"))
    while True:
        print("\n1. Play Game")
        print("2. View Game History")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            player_one = input("\nEnter player 1 name: ")
            player_two = input("Enter player 2 name: ")
            stats, rounds = play_game(player_one, player_two)
            save_stats(stats, rounds, player_one, player_two)
        elif choice == '2':
            view_history()
        elif choice == '3':
            print("Exiting the game. Thank you for playing!")
            os._exit(0)  # This will exit the program and close the console
        else:
            print("Invalid choice. Please select again.")

def main():
    welcome_page()

if __name__ == "__main__":
    main()
