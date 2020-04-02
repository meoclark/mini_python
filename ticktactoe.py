from IPython.display import clear_output 
def display_board(board):
    clear_output()                       
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[3]+'|'+board[2]+'|'+board[1])
test_board  = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

def win_check(board,marker):
    
    return ((board[7] == board[8] == board[9]  == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[1] == board[2] == board[3] == marker) or
    (board[7] == board[4] == board[1] == marker) or
    (board[8] == board[5] == board[2] == marker) or
    (board[9] == board[6] == board[3] == marker) or
    (board[7] == board[5] == board[3] == marker) or
    (board[9] == board[5] == board[1] == marker))
     
test_board  = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

def player_input():
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or 0: ').upper()
        
        if marker == 'X':
            
            return ('X','O')
        else:
            return ('O','X')
    
player1_maker ,player_maker , = player_input()

def place_maker(board, marker, position):
    board[position] = marker
place_maker(test_board,'$',8)
display_board(test_board)

def win_check(board,marker):
    
    return ((board[7] == board[8] == board[9]  == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[1] == board[2] == board[3] == marker) or
    (board[7] == board[4] == board[1] == marker) or
    (board[8] == board[5] == board[2] == marker) or
    (board[9] == board[6] == board[3] == marker) or
    (board[7] == board[5] == board[3] == marker) or
    (board[9] == board[5] == board[1] == marker))
    
    
display_board(test_board)
win_check(test_board,'X')


import random
def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board,position):
    
    return board[position] == ' '
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
        
    return position
def replay():
    
    choice = input("Play again? Enter Yes or No")
    
    return choice == 'Yes'
print('Welcome to Tic Tac Toe!')
 
while True:
    
    the_board = [' ']*10
    player1_maker,player2_maker = player_input()
    
    turn = choose_first()
    print(turn + 'will go first')
    
    play_game = input('Ready to play? y or n? ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn == 'Player 1':
            
            display_board(the_board)
                
            position = player_choice(the_board)
            
            place_maker(the_board,player1_maker,position)
            
            if win_check(the_board,player1_maker):
                display_board(the_board)
                print('PLAYER 1 HAS WON! !')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = 'Player 2'
                    
        else:
            display_board(the_board)
                
            position = player_choice(the_board)
            
            place_maker(the_board,player2_maker,position)
            
            if win_check(the_board,player2_maker):
                display_board(the_board)
                print('PLAYER 2 HAS WON! 1')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = 'Player 1'
                    
    if not replay():
        break
                
                
    
    