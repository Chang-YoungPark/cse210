import random

class Card:
    '''
    A deck of cards with a different numbers from 1-13.
    The resposibility of Card is ramdomly choose a card from 1 -13.

    '''
    
    def __init__(self):
        '''
        Construct a new instance of Card.
        '''
        self.current_card = 0
        self.last_card = 0

    def deal_card(self):
        '''
        Generates a ramdom card.
        '''
        self.last_card = self.current_card
        self.current_card = random.randint(1,13)