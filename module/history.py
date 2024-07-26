import time
import os

history_log = "history_log.txt"

def save_stats(stats, rounds, player_one, player_two):
    # Generate a unique filename using the current timestamp
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    html_filename = f"game_history_{timestamp}.html"
    txt_filename = f"game_history_{timestamp}.txt"
    
    # Save HTML format
    with open(html_filename, "w") as file:
        file.write("<!DOCTYPE html>\n")
        file.write("<html>\n<head>\n<title>Tic Tac Toe Game Results</title>\n")
        file.write("<style>\n")
        file.write("body { font-family: Arial, sans-serif; background-color: #f0f0f0; color: #333; text-align: center; padding: 50px; }\n")
        file.write(".container { background-color: #fff; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); display: inline-block; padding: 20px 40px; text-align: left; }\n")
        file.write("h1 { font-size: 24px; margin-bottom: 20px; }\n")
        file.write(".result { margin: 10px 0; font-size: 18px; }\n")
        file.write(".player { font-weight: bold; }\n")
        file.write("</style>\n")
        file.write("</head>\n<body>\n")
        file.write("<div class=\"container\">\n")
        file.write(f"<h1>Game Results</h1>\n")
        file.write(f"<div class=\"result\"><span class=\"player\">Game between:</span> {player_one} and {player_two}</div>\n")
        file.write(f"<div class=\"result\"><span class=\"player\">How many rounds in session:</span> {len(rounds)}</div>\n")
        file.write(f"<div class=\"result\"><span class=\"player\">Player {player_one} wins:</span> {stats['player_one_wins']}</div>\n")
        file.write(f"<div class=\"result\"><span class=\"player\">Player {player_two} wins:</span> {stats['player_two_wins']}</div>\n")
        file.write(f"<div class=\"result\"><span class=\"player\">Draws:</span> {stats['draws']}</div>\n")
        file.write("</div>\n</body>\n</html>\n")
    
    # Save TXT format
    with open(txt_filename, "w") as file:
        file.write("Tic Tac Toe Game Results\n")
        file.write(f"Game between: {player_one} and {player_two}\n")
        file.write(f"How many rounds in session: {len(rounds)}\n")
        file.write(f"Player {player_one} wins: {stats['player_one_wins']}\n")
        file.write(f"Player {player_two} wins: {stats['player_two_wins']}\n")
        file.write(f"Draws: {stats['draws']}\n")
    
    # Log the filenames
    with open(history_log, "a") as log_file:
        log_file.write(txt_filename + "\n")
        log_file.write(html_filename + "\n")

    print(f"Game stats saved to {html_filename} and {txt_filename}")

def view_history():
    try:
        with open(history_log, "r") as log_file:
            filenames = log_file.readlines()
        
        txt_files = [fname.strip() for fname in filenames if fname.strip().endswith('.txt')]
        
        if txt_files:
            print("\nFull Game History (TXT):")
            for fname in txt_files:
                try:
                    with open(fname, "r") as file:
                        print(f"\nHistory from {fname}:\n")
                        print(file.read())
                except FileNotFoundError:
                    print(f"Error: File {fname} not found. It may have been deleted or moved.")
        else:
            print("No TXT history files found.")
        
    except FileNotFoundError:
        print("Error: History log file not found. It may have been deleted or moved.")
