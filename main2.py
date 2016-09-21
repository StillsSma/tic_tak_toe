def menu():
    print("Welcome to Tic Tak Toe!")
    print ("First player to move is X.  Second is O")




def playermove():
    turn = 1
    while True:

        board = [["0,2","1,2","2,2"],
                 ["0,1","1,1","2,1"],
                 ["0,0","1,0","2,0"]]

        player = input("choose your position: ")
        for indices, rows in list(enumerate(board)):
            for indices2, locations in list(enumerate(rows)):
                if player == locations:
                    board[indices][indices2] == "X"
        print (board)
        turn = turn * -1

def game():
    menu()
    playermove()










game()
