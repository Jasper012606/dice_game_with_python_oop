from number_of_players import NumberOfPlayers
from game import Game

class MainMenu:
    def __init__(self):
        print("Welcome to the Dice Game!🎲\n 1). Start Game\t\t2). Exit Game")
    
    def show_main_menu(self):
        while True:
            user_input = input("Please enter your choice: ")
            if user_input == "2": 
                print("Exiting the game. Goodbye!")
                exit()
                
            elif user_input == "1":
                self.start_game()
            else:
                print("Invalid input. Please enter a number between 1 and 2.")
                continue
            
    def start_game(self):
        print("\nStarting the game...\n**GAME MECHANICS** In this dice game, 2 to 4 players can join by first entering the number of participants. Each player starts with a score of 0. Players take turns deciding whether to roll a die. If a player chooses to roll and gets a number between 2 and 6, that number is added to their score. However, if they roll a 1, their score resets to 0. Players may also choose to skip their turn. The game continues in turns until one player reaches a score of 50 or more, winning the game.\n")
        while True:
            number = input("Please enter the number of players (2-4): ")
            players = NumberOfPlayers(number)
            if players.check_if_valid():
                break
            
        dice = Game(players.number_of_players)
        dice.run(dice.roll)