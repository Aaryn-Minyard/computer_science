class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def win_percentage(self):
        return self.wins / (self.wins + self.losses)
    
    def print_standing(self):
        print(f'{self.name} has a winning percentage of {self.win_percentage():.2f}')


if __name__ == "__main__":
    team = Team()
   
    user_name = input("Enter team name: ")
    user_wins = int(input("Enter number of wins: "))
    user_losses = int(input("Enter number of losses: "))
    
    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses
    
    team.print_standing()