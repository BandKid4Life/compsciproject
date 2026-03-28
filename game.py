# ==========================================
# Number game
# ==========================================
# Features:
# - Control Loops
# - Data Types
# - Lists, Tuples, Dictionaries
# - Functions
# - Exception Handling
# - Object-Oriented Programming
# - Colored UI
# - Score System
# - Leaderboard
# - Replay System
# - Hint System

import random
import os
import time

# ================= COLORS =================
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

# ================= PLAYER CLASS =================
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.guess_history = []  # list

    def add_score(self, points):
        self.score += points

    def add_guess(self, guess):
        self.guess_history.append(guess)

# ================= GAME CLASS =================
class GuessingGame:
    def __init__(self):
        self.leaderboard = {}  # dictionary

    # ---------- Utility ----------
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def slow_print(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.01)
        print()

    def header(self):
        print(Colors.CYAN + "\n==============================")
        print("   NUMBER GUESSING GAME")
        print("==============================" + Colors.RESET)

    # ---------- Difficulty ----------
    def choose_difficulty(self):
        print(Colors.YELLOW + "\nChoose Difficulty:" + Colors.RESET)
        print("1. Easy (1-10, 5 tries)")
        print("2. Medium (1-50, 7 tries)")
        print("3. Hard (1-100, 10 tries)")

        choice = input("Enter choice: ")

        if choice == '1':
            return (10, 5)
        elif choice == '2':
            return (50, 7)
        elif choice == '3':
            return (100, 10)
        else:
            print(Colors.RED + "Invalid choice! Defaulting to Easy." + Colors.RESET)
            return (10, 5)

    # ---------- Hint System ----------
    def give_hint(self, guess, number):
        if abs(guess - number) <= 5:
            print(Colors.GREEN + "Very close!" + Colors.RESET)
        elif abs(guess - number) <= 15:
            print(Colors.YELLOW + "Close!" + Colors.RESET)
        else:
            print(Colors.RED + "Far away!" + Colors.RESET)

    # ---------- Play Round ----------
    def play_round(self, player):
        max_num, attempts = self.choose_difficulty()
        number = random.randint(1, max_num)

        print(Colors.BLUE + f"\nGuess a number between 1 and {max_num}" + Colors.RESET)

        for attempt in range(1, attempts + 1):
            try:
                guess = int(input(f"Attempt {attempt}/{attempts}: "))
            except ValueError:
                print(Colors.RED + "Invalid input! Enter a number." + Colors.RESET)
                continue

            player.add_guess(guess)

            if guess == number:
                print(Colors.GREEN + "Correct!" + Colors.RESET)
                points = (attempts - attempt + 1) * 10
                player.add_score(points)
                print(Colors.GREEN + f"Points earned: {points}" + Colors.RESET)
                return True

            elif guess < number:
                print(Colors.YELLOW + "Too low!" + Colors.RESET)
            else:
                print(Colors.YELLOW + "Too high!" + Colors.RESET)

            self.give_hint(guess, number)

        print(Colors.RED + f"\nYou lost! Number was {number}" + Colors.RESET)
        return False

    # ---------- Leaderboard ----------
    def update_leaderboard(self, player):
        self.leaderboard[player.name] = player.score

    def show_leaderboard(self):
        print(Colors.CYAN + "\n=== LEADERBOARD ===" + Colors.RESET)
        sorted_board = sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)
        for name, score in sorted_board:
            print(f"{name}: {score}")

    # ---------- Stats ----------
    def show_stats(self, player):
        print(Colors.BLUE + "\n=== PLAYER STATS ===" + Colors.RESET)
        print(f"Name: {player.name}")
        print(f"Score: {player.score}")
        print(f"Guesses: {player.guess_history}")

    # ---------- Menu ----------
    def menu(self):
        print("\n1. Play Game")
        print("2. Leaderboard")
        print("3. Player Stats")
        print("4. Reset Score")
        print("5. Exit")

    # ---------- Reset ----------
    def reset_score(self, player):
        confirm = input("Reset score? (y/n): ")
        if confirm.lower() == 'y':
            player.score = 0
            player.guess_history.clear()
            print(Colors.GREEN + "Score reset!" + Colors.RESET)
        else:
            print("Cancelled.")

    # ---------- Run Game ----------
    def run(self):
        self.clear_screen()
        self.header()

        name = input("Enter your name: ")
        player = Player(name)

        while True:  # main loop
            self.menu()
            choice = input("Select option: ")

            if choice == '1':
                self.play_round(player)
                self.update_leaderboard(player)

            elif choice == '2':
                self.show_leaderboard()

            elif choice == '3':
                self.show_stats(player)

            elif choice == '4':
                self.reset_score(player)

            elif choice == '5':
                print(Colors.CYAN + "Thanks for playing!" + Colors.RESET)
                break

            else:
                print(Colors.RED + "Invalid choice!" + Colors.RESET)

# ================= MAIN =================
if __name__ == "__main__":
    game = GuessingGame()
    game.run()

# ==========================================
#
#
#
# End of Game
