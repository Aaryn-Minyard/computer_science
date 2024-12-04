import random

class RockPaperScissors:
    def __init__(self):
        self.player1 = 40
        self.player2 = 40
        self.rounds = 0
        self.player1_wins = 0
        self.player2_wins = 0
        self.choices = {0: "rock", 1: "paper", 2: "scissors"}

    def get_player1_health(self):
        return self.player1

    def get_player2_health(self):
        return self.player2

    def get_rounds(self):
        return self.rounds

    def get_player1_wins(self):
        return self.player1_wins

    def get_player2_wins(self):
        return self.player2_wins

    def play_round(self):
        self.rounds += 1
        
        try:
            player1_choice = int(input("Player 1, enter your choice (rock[0], paper[1], or scissors[2]): "))
            if player1_choice not in self.choices:
                print("Invalid choice. Please enter 0 for rock, 1 for paper, or 2 for scissors.")
                self.rounds -= 1  # Do not count this as a valid round
                return
        except ValueError:
            print("Invalid input. Please enter a number (0 for rock, 1 for paper, or 2 for scissors).")
            self.rounds -= 1  # Do not count this as a valid round
            return
        player2_choice = random.randint(0, 2)

        # Print player choices using the dictionary
        print(f"Player 1 chose: {self.choices[player1_choice]}")
        print(f"Player 2 chose: {self.choices[player2_choice]}")

        if player1_choice == player2_choice:
            print("It's a tie!")
            return
        elif player1_choice == 0 and player2_choice == 1:
            self.player1 -= 20
            self.player2_wins += 1
            print("Player 2 wins this round!")
        elif player1_choice == 0 and player2_choice == 2:
            self.player2 -= 20
            self.player1_wins += 1
            print("Player 1 wins this round!")
        elif player1_choice == 1 and player2_choice == 0:
            self.player2 -= 20
            self.player1_wins += 1
            print("Player 1 wins this round!")
        elif player1_choice == 1 and player2_choice == 2:
            self.player1 -= 20
            self.player2_wins += 1
            print("Player 2 wins this round!")
        elif player1_choice == 2 and player2_choice == 0:
            self.player1 -= 20
            self.player2_wins += 1
            print("Player 2 wins this round!")
        elif player1_choice == 2 and player2_choice == 1:
            self.player2 -= 20
            self.player1_wins += 1
            print("Player 1 wins this round!")

if __name__ == "__main__":
    game = RockPaperScissors()
    while game.get_player1_health() > 0 and game.get_player2_health() > 0:
        game.play_round()
        
    if game.get_player1_health() == 0:
        print("Player 2 wins the game!")
    else:
        print("Player 1 wins the game!")
    print("Number of rounds played:", game.get_rounds())
    print("Number of rounds won by Player 1:", game.get_player1_wins())
    print("Number of rounds won by Player 2:", game.get_player2_wins())
