#W02 Tic-Tac-Toe
#author : ChangYoung Park

#1|2|3
#-+-+-
#4|5|6
#-+-+-
#7|8|9

def main():
    user = 'o'
    game = make_tic_tac_toe()
    while not(check_win(game)) :    
        print_tic_tac_toe(game)        
        question = user + "'s turn to choose a square (1-9): "
        value = int(input(question)) 
        value = value - 1
        game[value] = user   
        user = user_turn(user)
       
    print_tic_tac_toe(game)    
    print("Good game. Thanks for playing!")  

#ask a question     
def user_turn(user):
    if user == 'x':
        user = 'o'
    else:
        user = 'x'   
    
    return user 

# make game
def make_tic_tac_toe():
    game = []
    
    for i in range(9):
        game.append(i + 1) 
    
    return game
  
#    print("1|2|3")
#    print("-+-+-")
#    print("4|5|6")
#    print("-+-+-")
#    print("7|8|9")
# print game
def print_tic_tac_toe(game) :
    print(f"{game[0]}|{game[1]}|{game[2]}")
    print(f"-+-+-")
    print(f"{game[3]}|{game[4]}|{game[5]}")
    print(f"-+-+-")
    print(f"{game[6]}|{game[7]}|{game[8]}")
 
# winner Check 
def check_win(game):
    if ( game[0] == game[1] == game[2] or
         game[3] == game[4] == game[5] or
         game[6] == game[7] == game[8] or
         game[0] == game[3] == game[6] or
         game[1] == game[4] == game[7] or
         game[2] == game[5] == game[8] or
         game[0] == game[4] == game[8] or
         game[2] == game[4] == game[6] ):
        return True
         

# Call main to start this program.
if __name__ == "__main__":
    main()       