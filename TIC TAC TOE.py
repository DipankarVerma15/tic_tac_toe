#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Created by Dipankar Verma

def the_board(board):
    print('  |    |')
    print(board[1]+' | ',board[2]+' |',board[3])
    print('----------')
    print('  |    |')
    print(board[4]+' | ',board[5]+' |',board[6])
    print('----------')
    print(board[7]+' | ',board[8]+' |',board[9])
    print('  |    |')
    
def win_check(board,mark):
    # returning should be opposte as loop
    # will end if win returns False
    return not ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


import random
def first():
    if random.randint(1,2)==1:
        return 'player 1'
    else:
        return 'player 2'
    
    
def marker():
    print('which marker you want to take X or O')
    c=''
    while c not in ('X','O'):
        c=input('Enter the marker you want to take input as:').upper()
    if c=='X':
        return('X','O')
    else:
        return('O','X')
    
def user_choise():
    choise='dipankar'
    while choise.isdigit()==False:
        choise=input("Enter a no between (1-10):")
    choise=int(choise)
    if choise in range(1,11):
        return choise
    else:
        user_choise()
        
def pen(player_marker,position,board):
    board[position]=player_marker
    
    
def available_space(board):
    disco=0
    for index,space in enumerate(board):
        if space==' ':
            print(index)
            disco+=1
        else:
            pass
    if disco>=1:
        return True
    else:
        return False
    
def chek_space(board,position):
    if board[position]==' ':
        return True
    else:
        return False
    
    

    
board=['',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1_marker,player2_marker=marker()
turn=first()
print(turn,'moves first')
game_on=True
while game_on:
    while turn=='player 1'and game_on:
    # there is no statement inside this loop which supposed to break the loop if a player wins therefore game_on condition is added
        the_board(board)
        game_on=available_space(board)
        #######
        print("Playe 1 chance") # Extras
        #######
        position=user_choise()
        space=chek_space(board,position)
        # moved win_check() below from here
        if space==True:
            pen(player1_marker,position,board)
            turn='player 2'
        else: 
            print('the position you want to mark at is already occupied')
            print('CHOOSE form the given no')
            available_space(board)
            
        game_on=win_check(
                      board,player1_marker)
# cheking if any player have won
        
    
        if not game_on: print("Player 1 wins")
       

    while turn=='player 2' and game_on: 
             # same here as above mentioned
        the_board(board)
        game_on=available_space(board)
        print("Player 2 chance")
        position=user_choise()
        dipu=chek_space(board,position)
        # moved win_check() below from here
        if dipu==True:
            pen(player2_marker,position,board)
            turn='player 1'
        else: 
            print('the position you want to mark at is already occupied')
            print('CHOOSE form the given no')
            available_space(board)
        game_on=win_check(
                    board,player2_marker)
# win should be checked after the board is modified
        
    
        if not game_on: print("Player 2 wins")
      
    

