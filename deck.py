from random import randint
class Deck:
    def __init__(self, shuffled = True):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.my_deck = []
        for suit in suits:
            for value in values:
                self.my_deck.append(f"{value} of {suit}")
        if shuffled:
            self.shuffle()

    def shuffle(self):
        old_deck = self.my_deck
        self.my_deck = []
        while len(old_deck) > 0:
            i = randint(0,len(old_deck)-1)
            self.my_deck.append(old_deck.pop(i))
    
    def get_value(self, card):
        split_string = card.split("of")
        value = split_string[0].strip()
        if value == "Ace":
            value = 1
        elif value == "Jack":
            value = 11
        elif value == "Queen":
            value = 12
        elif value == "King":
            value = 13
        else:
            value = int(value)
        return value

