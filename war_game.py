import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
#create card class
class Card:
    def __init__(self, suit, ranks):
        self.suit = suit
        self.rank = ranks
        self.value = values[ranks]
    def show(self):
        print('{} of {}'.format(self.rank, self.suit))

#create Deck class
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def show(self):
        for card in self.cards:
            card.show()
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()

deck = Deck()
deck.shuffle()
deck.show()
mycard = deck.deal_one()
mycard.show()