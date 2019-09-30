
# coding: utf-8

# In[ ]:


from IPython.display import clear_output

def display_board(board):
    a1 = board[0]
    a2 = board[1]
    a3 = board[2]
    a4 = board[3]
    a5 = board[4]
    a6 = board[5]
    a7 = board[6]
    a8 = board[7]
    a9 = board[8]
    print(f'_{a1}_|_{a2}_|_{a3}_ \n_{a4}_|_{a5}_|_{a6}_ \n {a7} | {a8} | {a9}') 

def player_input():
    global player1
    global player2
    while True:
        print("Let's play TicTocToe Game!")
        player1 = input('Player1 Please choose X or O: ')
        clear_output()
        if player1 == 'X':
            player2 = 'O'
            print ('Player1 -> X \nPlayer2 -> O.')
            break
        elif player1 == 'O':
            print ('Player1 -> O \nPlayer2 is X. ')
            player2 = 'X'
            break 
        else:
            print ('Wrong Input please try again!')
            return

#check if has space to continue the game 
def check_board(board):
    
    flag = 0
    for i in board:
        if i != ' ':
            flag += 1
        else:
            continue
def replay():
    while True:
        replay = input('Replay? Y/N:')
        if replay == 'Y':
            clear_output()
            return True
            break
        elif replay == 'N':
            clear_output()
            return False
            break
        else:
            clear_output()
            print('Wrong Input, Please Try again: ')
            continue
        
def check_win(board):
    global win
    win = False
    if (board[0] == board[1] == board[2] != ' ' or 
        board[3] == board[4] == board[5] != ' ' or 
        board[6] == board[7] == board[8] != ' ' or
        board[0] == board[3] == board[6] != ' ' or 
        board[1] == board[4] == board[7] != ' ' or 
        board[2] == board[5] == board[8] != ' ' or
        board[0] == board[4] == board[8] != ' ' or
        board[2] == board[4] == board[6] != ' '):
        win = True 
        return win
    else:
        win = False
        return win
    
#Start

global FLG
FLG = True
while FLG:
    game_on = True
    global board
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']     
    player_input()
    while game_on:
        #Player 1 Turn
        p1_turn = int(input('P1 Turn：'))
        clear_output()
        board[p1_turn -1] = player1
        display_board(board)
        check_win(board)
        #check_board(board)
        if win == False:
            print('Continue Game')

        else:
            print('Game Over, P1 Win! ')
            replay()
            if True:
                break # jump out of game_one loop
            else:
                break # jump out of game_one loop
                FLG = False 
            #break # jump out of Big loop
        # Player2's turn.
        p2_turn = int(input('P2 Turn：'))
        clear_output()
        board[p2_turn -1] = player2
        display_board(board)
        check_win(board)
        #check_board(board)
        if win == False:
            print('Continue Game')

        else:
            print('Game Over P2 Win!')
            replay()
            if True:
                break # jump out of game_one loop
            else:
                break # jump out of game_one loop
                FLG = False 

