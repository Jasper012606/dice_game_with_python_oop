from number_of_players import NumberOfPlayers
from dice import Dice

class Game(Dice):
    def __init__(self, number_of_players, max_score=50):
        self.number_of_players = number_of_players
        self.max_score = max_score
        self.player_scores = [0 for _ in range(self.number_of_players)]




                
