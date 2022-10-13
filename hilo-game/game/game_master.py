import sys
from game.card import Card

class Game_master:
    def __init__(self):
        self.isPlaying = True
        self.score = 300
        self.card = Card()
        self.card.deal_card()
        

    def start_game(self):

        print('''\n
        Welcome to Hilo Game! 
        -----------------------
        
        You have 300 worth of points.
        Guess if the next card is higher or lower to earn more points.
        If your guess is correct you can earn 100 points but if not
        75 points will be deducted from your score. Have fun!!!!''')
        
        while self.isPlaying:
            self.get_input()
            self.update_score()
            self.output_score()

    def get_input(self):

        last = self.card.current_card # deal ramdom card
        print(f'\nThe card is: {last}')

        self.user_choice = input('Higher / Lower? [h/l]: ').lower() # user choose high or low
        while self.user_choice != 'h' and self.user_choice != 'l':
            self.user_choice = input('Higher / Lower? [h/l]: ').lower()

    def update_score(self):
        '''Update the score of the player'''
        self.card.deal_card()

        new_card = self.card.current_card
        last_card = self.card.last_card

        while new_card == last_card:
            self.card.deal_card()

            new_card = self.card.current_card
            last_card = self.card.last_card


        if new_card > last_card and self.user_choice == 'h' or new_card < last_card and self.user_choice == 'l':
            self.score += 100
            message = 'Good job!'
        else:
            self.score -=75
            message = 'Oh no!'
        
        print(message)
        print(f'The new card is: {new_card}.')

    def output_score(self):
        
        print(f'Your score is: {self.score}')
        
        if self.score > 0:
            play_again = input('Enter [Y] to play again: ').lower()
            if play_again == 'y':
                self.isPlaying = True
            
            else:
                print('\nThank you for playing. Play again next time.')
                sys.exit()
        
        else:
            print('\nGame Over! Thank you for playing HILO.')
            sys.exit()
            
