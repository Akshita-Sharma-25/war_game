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
        
    
#player class
class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def deal(self):
        return self.all_cards.pop(0)
    def add(self,newcard):
        if isinstance(newcard,list):
            self.all_cards.extend(newcard)
        else:
            self.all_cards.append(newcard)
    def __str__(self):
        return f'the player {self.name} has {len(self.all_cards)} cards'

deck=Deck()
deck.shuffle()
player1=Player('one')
player2=Player('two')
n=len(deck.cards)
for i in range(n//2):
    player1.add(deck.deal_one())
    player2.add(deck.deal_one())
print(player1)
print(player2)
game_on=True
while game_on:
    
    if len(player1.all_cards)==0:
        print('Player 2 win!')
        game_on=False
        break
    if len(player2.all_cards)==0:
        print('Player 1 win!')
        game_on=False
        break
    player1_cards=[]
    player2_cards=[]
    player1_cards.append(player1.deal())
    player2_cards.append(player2.deal())
    at_war=True
    while at_war:
        
        if player1_cards[-1].value>player2_cards[-1].value:
            player1.add(player1_cards)
            player1.add(player2_cards)
            at_war=False
        elif player2_cards[-1].value>player1_cards[-1].value:
            player2.add(player1_cards)
            player2.add(player2_cards)
            at_war=False
        
            






