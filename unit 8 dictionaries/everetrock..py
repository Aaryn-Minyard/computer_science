import tkinter as tk
from random import choice

# Define game options in a structured dictionary
game_options = {
    "Rock": {"beats": ["Scissors", "Lizard", "Fire"], "ties": ["Rock"], "loses": ["Paper", "Spock", "Chuck Norris"]},
    "Paper": {"beats": ["Rock", "Glock", "Earth"], "ties": ["Paper"], "loses": ["Scissors", "Lizard", "Fire"]},
    "Scissors": {"beats": ["Paper", "Lizard", "Air"], "ties": ["Scissors"], "loses": ["Rock", "Spock", "Chuck Norris"]},
    "Lizard": {"beats": ["Spock", "Paper", "Earth"], "ties": ["Lizard"], "loses": ["Rock", "Scissors", "Fire"]},
    "Spock": {"beats": ["Rock", "Scissors", "Glock"], "ties": ["Spock"], "loses": ["Paper", "Lizard", "Chuck Norris"]},
    "Glock": {"beats": ["Fire", "Darkness", "Alien"], "ties": ["Glock"], "loses": ["Water", "Paper", "Chuck Norris"]},
    "Batman": {"beats": ["Alien", "Darkness", "Spock"], "ties": ["Batman"], "loses": ["Fire", "Bruce Willis", "Chuck Norris"]},
    "Bruce Willis": {"beats": ["Batman", "Alien", "Light"], "ties": ["Bruce Willis"], "loses": ["Water", "Air", "Chuck Norris"]},
    "Fire": {"beats": ["Batman", "Earth", "Darkness"], "ties": ["Fire"], "loses": ["Water", "Rock", "Chuck Norris"]},
    "Water": {"beats": ["Fire", "Bruce Willis", "Earth"], "ties": ["Water"], "loses": ["Air", "Alien", "Chuck Norris"]},
    "Air": {"beats": ["Water", "Earth", "Light"], "ties": ["Air"], "loses": ["Darkness", "Glock", "Chuck Norris"]},
    "Earth": {"beats": ["Air", "Darkness", "Alien"], "ties": ["Earth"], "loses": ["Fire", "Water", "Chuck Norris"]},
    "Light": {"beats": ["Darkness", "Alien", "Air"], "ties": ["Light"], "loses": ["Bruce Willis", "Earth", "Chuck Norris"]},
    "Darkness": {"beats": ["Light", "Earth", "Batman"], "ties": ["Darkness"], "loses": ["Fire", "Water", "Chuck Norris"]},
    "Chuck Norris": {"beats": ["Rock", "Paper", "Scissors", "Lizard", "Spock", "Glock", "Batman", "Bruce Willis", "Fire", "Water", "Air", "Earth", "Light", "Darkness", "Alien"], "ties": ["Chuck Norris"], "loses": []},  # Chuck Norris beats all except himself
}

# Game settings
player_health = 5
computer_health = 5

def add_option(name, beats, ties, loses):
    game_options[name] = {"beats": beats, "ties": ties, "loses": loses}

def delete_option(name):
    if name in game_options:
        del game_options[name]

# GUI Implementation
class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors, and Beyond")
        self.frame = tk.Frame(root)
        self.frame.pack()

        # Health bars
        self.player_health = player_health
        self.computer_health = computer_health
        self.create_health_bar()

        # Display options
        self.create_options()

    def create_health_bar(self):
        self.player_health_label = tk.Label(self.frame, text=f"Player Health: {self.player_health}")
        self.player_health_label.pack()
        self.computer_health_label = tk.Label(self.frame, text=f"Computer Health: {self.computer_health}")
        self.computer_health_label.pack()

    def create_options(self):
        tk.Label(self.frame, text="Choose your move:").pack()
        for option in game_options.keys():
            tk.Button(self.frame, text=option, command=lambda opt=option: self.play_round(opt)).pack()

    def play_round(self, player_choice):
        computer_choice = choice(list(game_options.keys()))
        outcome = self.determine_outcome(player_choice, computer_choice)

        # Show result screen
        self.show_result(player_choice, computer_choice, outcome)

        # Update health
        if outcome == "Lose":
            self.player_health -= 1
        elif outcome == "Win":
            self.computer_health -= 1

        # Check for game over
        if self.player_health == 0 or self.computer_health == 0:
            self.show_game_over()

    def determine_outcome(self, player, computer):
        if computer in game_options[player]["beats"]:
            return "Win"
        elif computer in game_options[player]["loses"]:
            return "Lose"
        else:
            return "Draw"

    def show_result(self, player, computer, outcome):
        result_window = tk.Toplevel(self.root)
        result_window.title("Round Result")
        tk.Label(result_window, text=f"You chose: {player}").pack()
        tk.Label(result_window, text=f"Computer chose: {computer}").pack()
        tk.Label(result_window, text=f"Result: {outcome}").pack()
        tk.Button(result_window, text="OK", command=result_window.destroy).pack()

    def show_game_over(self):
        result_window = tk.Toplevel(self.root)
        result_window.title("Game Over")
        winner = "Player" if self.computer_health == 0 else "Computer"
        tk.Label(result_window, text=f"Game Over! {winner} wins!").pack()
        tk.Button(result_window, text="Exit", command=self.root.quit).pack()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
