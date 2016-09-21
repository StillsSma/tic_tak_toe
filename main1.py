def menu():
    print("Welcome to Tic Tak Toe!")
    print ("First player to move is X.  Second is O")

def display():
    for rows in board:
        print(rows)


board = [["0,0","1,0","2,0"],
         ["0,1","1,1","2,1"],
         ["0,2","1,2","2,2"]]

def playermove():
    turn = 1
    while True:
        player = input("choose your position: ")
        for indices, rows in list(enumerate(board)):
            for indices2, locations in list(enumerate(rows)):
                if locations == player:
                    if turn == 1:
                        board[indices][indices2] = "X"
                    else:
                        board[indices][indices2] = "O"
        display()
        turn = turn * -1
        for rows in board:
            if rows == ["X","X","X"] or rows == ["O","O","O"]:
                print ("Game Over!")
                answer = input("Play Again? y/n: ")
                if answer == "y":
                    menu()
                else:
                    exit()

def game():
    menu()
    playermove()


game()
