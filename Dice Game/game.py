from number_of_players import NumberOfPlayers
from dice import Dice

class Game(Dice):
    def __init__(self, number_of_players, max_score=50):
        self.number_of_players = number_of_players
        self.max_score = max_score
        self.player_scores = [0 for _ in range(self.number_of_players)]
        
    def run(self, roll):
        while max(self.player_scores) < self.max_score:
            for player_idx in range(self.number_of_players):
                print("\nPlayer number", player_idx + 1, "turn has just started!")
                print("Your total score is:", self.player_scores[player_idx], "\n")
                current_score = 0
        



                
