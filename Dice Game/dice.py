#import the random module
import random 

#make a class that returns a random number between 1 and 6
class Dice:
    def roll(self, min_value=1, max_value=6):
        roll = random.randint(min_value, max_value)
        return roll
    
value = Dice()
print(value.roll())  # Example usage, prints a random number between 1 and 6
        