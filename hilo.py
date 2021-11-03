from deck import Deck
class Hilo_Game:
    def __init__(self):
        self.deck = Deck()
        self.points = 300
        self.top_card = self.deck.my_deck.pop(0)
        self.exit = False
        self.user_input = ""

    def game_loop(self):
        while not self.exit:
            self.get_input()
            self.show_higher_lower()
            self.cont()
            if len(self.deck.my_deck) < 1:
                self.exit = True
        print(f"Your score is {self.points}! Thank you for playing.")

    def get_input(self):
        print(f"The card is the {self.top_card}. Will the next one be higher or lower? (h/l)")
        self.user_input = input(">> ")

    def cont(self):
        do_cont = input(f"You have {self.points} points. Do you want to continue?(y/n) \n>> ")
        if do_cont == "n":
            self.exit = True 

    def show_higher_lower(self):
        old_value = self.deck.get_value(self.top_card)
        self.top_card = self.deck.my_deck.pop(0)
        new_value = self.deck.get_value(self.top_card)
        print(new_value, old_value)
        if new_value > old_value:
            if self.user_input == "h":
                print(f"The next card was {self.top_card}! You win 100 points.")
                self.points += 100
            else:
                print(f"The next card was {self.top_card}. You lose 75 points.")
                self.points -= 75
        elif new_value < old_value:
            if self.user_input == "l":
                print(f"The next card was {self.top_card}! You win 100 points.")
                self.points += 100
            else:
                print(f"The next card was {self.top_card}. You lose 75 points.")
                self.points -= 75
        else:
            print(f"The next card was {self.top_card}. You lose 75 points.")
            self.points -= 75

