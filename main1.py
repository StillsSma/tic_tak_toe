def menu():
    print("Welcome to Tic Tak Toe!")
    print ("First player to move is X.  Second is O")

def end():
    choice = input("Game over, would you like to play again? y/n ")
    if choice == "y":
        game()
    else:
        exit()
def display_board(board):
    print(" " + '0' + "  " + '1' + "  " + '2')
    print("0 " + board[0]['0,0'] + '|' + board[0]['1,0'] + '|' + board[0]['2,0'])
    print("  -+-+-")
    print("1 " + board[1]['0,1'] + '|' + board[1]['1,1'] + '|' + board[1]['2,1'])
    print("  -+-+-")
    print("2 " + board[2]['0,2'] + '|' + board[2]['1,2'] + '|' + board[2]['2,2'])

def end_condition(board):
    for dicts in board:
        if all(x== "X" for x in dicts.values()) or all(x== "O" for x in dicts.values())  == True:
            end()
    columns = [ [board[0]['0,0'],board[1]['0,1'],board[2]['0,2']],
                [board[0]['1,0'],board[1]['1,1'],board[2]['1,2']],
                [board[0]['2,0'],board[1]['2,1'],board[2]['2,2']]]

    for column in columns:
        if all(x== "X" for x in column) or all(x== "O" for x in column) == True:
            end()
    diagonals = [[board[0]['0,0'],board[1]['1,1'],board[2]['2,2']],
                [board[2]['0,2'],board[1]['1,1'], board[0]['2,0']]]
    for diagonal in diagonals:
        if all(x== "X" for x in diagonal) or all(x== "O" for x in diagonal) == True:
            end()


def game():
    board = [{"0,0": " ","1,0": " ","2,0": " "},
             {"0,1": " ","1,1": " ","2,1": " "},
             {"0,2": " ","1,2": " ","2,2" :" "}]



    menu()
    display_board(board)
    turn = 1
    while True:
        playermove(turn,board)
        display_board(board)
        end_condition(board)
        turn = turn * -1


def playermove(turn,board):
    player = input("choose your position(x,y) ")
    legal_moves = ['0,0','1,0','2,0','0,1','1,1','2,1','0,2','1,2','2,2']
    if player not in legal_moves:
        print ("That is not a valid move")
        playermove(turn,board)

    for dicts in board:
        for keys in dicts:
            if keys == player:
                if turn == 1:
                    dicts[keys] = "X"
                else:
                    dicts[keys] = "O"


board = [{"0,0": " ","1,0": " ","2,0": " "},
         {"0,1": " ","1,1": " ","2,1": " "},
         {"0,2": " ","1,2": " ","2,2" :" "}]

game()
