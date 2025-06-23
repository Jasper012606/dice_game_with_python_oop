class NumberOfPlayers:
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        
    def check_if_valid(self):
            if self.number_of_players.isdigit():
                self.number_of_players = int(self.number_of_players)
                if 2 <= self.number_of_players <= 4:
                    return self.number_of_players
                else:
                    print("Players must be between 2 and 4.")
            else:
                print("Input invalid, please enter a number between 2 and 4.")