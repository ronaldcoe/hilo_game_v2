from deck import Deck
class Hilo_Game:
    def __init__(self):
        self.deck = Deck()
        self.points = 300
        self.top_card = self.deck.my_deck.pop(0)
        self.exit = False
        self.input_validation = False
        self.cont_validation = False
        self.user_input = ""

    def show_instructions(self):
        print(100*"-")
        print("Welcome to the Hilo Game")
        print("\nInstructions")
        print("You will start the game with 300 points. The dealer will show you the current card.\nYou will need to guess if the next one will be higher (h) or lower (l).\nThe dealer will show you the next card. You will earn 100 points if you guessed correctly, but you will\nlose 75 points if you guessed incorrectly. If you lose 0 all of your points, the game is over.\nOtherwise the game will continue until you decide to end it by entering (e) at any point in the game.\nGood Luck!")
        print(100*'-')    

    def game_loop(self):
        while not self.exit:
            self.get_input()
            self.show_higher_lower()
            if len(self.deck.my_deck) < 1 or self.points <= 0:
                self.exit = True
                self.points = 0
            elif self.user_input.lower() == "e":
                self.exit = True             
        print(f"Your score is {self.points}! Thank you for playing.")


    def get_input(self):
        while not self.input_validation:        
            print(f"The card is the {self.top_card}. Will the next one be higher or lower? (h/l)")
            self.user_input = input(">> ")
            if self.user_input.lower() == "h" or self.user_input.lower() == "l":
                self.input_validation = True
            elif self.user_input.lower() == "e":
                self.input_validation = True
            else:
                print("Sorry, that is not a valid response. Let's try again")
                self.input_validation = False
        self.input_validation = False


    def show_higher_lower(self):
        old_value = self.deck.get_value(self.top_card)
        self.top_card = self.deck.my_deck.pop(0)
        new_value = self.deck.get_value(self.top_card)
        if self.user_input != 'e':
            if new_value > old_value:
                if self.user_input == "h":
                    self.points += 100
                    print(f"The next card was {self.top_card}! You win 100 points.\nYou have {self.points} points.")
                    
                else:
                    self.points -= 75
                    print(f"The next card was {self.top_card}. You lose 75 points.\nYou have {self.points} points.")
                    
            elif new_value < old_value:
                if self.user_input == "l":
                    self.points += 100
                    print(f"The next card was {self.top_card}! You win 100 points.\n You have {self.points} points.")
                    
                else:
                    self.points -= 75
                    print(f"The next card was {self.top_card}. You lose 75 points.\n You have {self.points} points.")
                    
            else:
                self.points -= 75
                print(f"The next card was {self.top_card}. You lose 75 points.\n You have {self.points} points.")
            

