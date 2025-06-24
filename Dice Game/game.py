from number_of_players import NumberOfPlayers
from dice import Dice

class Game(Dice):
    def __init__(self, number_of_players, max_score=50):
        self.number_of_players = number_of_players
        self.max_score = max_score
        self.player_scores = [0 for numbers in range(self.number_of_players)]
        
    def run(self, roll):
        while max(self.player_scores) < self.max_score:
            for player_idx in range(self.number_of_players):
                print("\nPlayer number", player_idx + 1, "turn has just started!")
                print("Your total score is:", self.player_scores[player_idx], "\n")
                current_score = 0
        
                while True:
                    should_roll = input("Would you like to roll (y/n)? ")
                    if should_roll.lower() != "y":
                        break
                    
                    value = roll()
                    if value == 1:
                        print("You rolled a 1! Turn done!")
                        current_score = 0
                        break
                    else:
                        current_score += value
                        print("You rolled a:", value)

                    print("Your score is:", current_score)

                self.player_scores[player_idx] += current_score
                print("Your total score is:", self.player_scores[player_idx])
                
        max_score = max(self.player_scores)
        winning_idx = self.player_scores.index(max_score)
        print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)
        print("Game's over! Thanks for playing!")
        exit()