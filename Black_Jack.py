import random as r


dec = []
suits = ["S", "H", "C", "D"]
nums = ["2", "3", "4", "5", "6", "7", '8', '9', "10", "J", "Q", "K", "A"]
def add_deck(dec):
    for suit in suits:
        for num in nums:
            dec.append((str(num) + "-" + str(suit)))
    return dec
    
add_deck(dec)
r.shuffle(dec)

print(dec)


class BlackJack(): # maybe amount of decs used
    def __init__(self, dec):
        self.dec = dec
        self.dealers_hand = []
        self.players_hand = []
        # create loop here that will play over and over and then reset decs as well as they run out
        self.play()
    
    def play(self):
        card = dec.pop
        print("Dealer's Card: " + str(card))
        card_1 = dec.pop
        card_2 = dec.pop
        print("your cards: " + str(card_1) + ", " + str(card_2))
        
        print("good starts")
        # create a dealer and player class?
        
        # draw 2 cards and show the dealers 1 
        
        # check for blackjack
        # give option to hit or pass
        
        # check if over 21 
         # then asks again to hit or pass, 
         # maybe dealer show another card here
         
         # after delaer show card
        
        
        pass
    
    def load_decs():
        pass
    
    def draw(): # or just use pop
        pass
    
    def check_deck_len():
        pass
    

BlackJack(dec)