import reversi
def main():
    game = reversi.Reversi()
    playColour = input("What colour do you want to be (b/w), black starts?: ")
    while playColour != "b" and playColour != "w":
            playColour = input("What colour do you want to be (b/w)?: ")
    game.setPlayerColour(playColour)
    difficulty = input("Enter 1 to set difficulty to easy, 2 to set difficulty to hard: ")
    while difficulty != "1" and difficulty != 2:
        difficulty = input("Enter 1 to set difficulty to easy, 2 to set difficulty to hard: ")
    flag = True
    while flag:
        game.displayBoard()
        print("Black has %d points, white has %d points" % (game.getScore("b"), game.getScore("w")))
        if game.getTurn() == playColour:
            if game.isGameOver():
                flag = False
            else:
                moveFlag = True
                while moveFlag:
                    move = input("Make a move with y axis first and x axis second separated by a space in the format: y x or type 'q' to quit. ->")
                    if move == 'q':
                        flag = False
                        moveFlag = False
                    else:
                        try:
                            valid = game.isPositionValid(tuple(map(int, move.split())), playColour)
                        except AssertionError as a:
                            print("Looks like you entered something wrong: ", a.args[0])
                        except ValueError:
                            print("You need to enter an integer between 0 and 7 for each coordinate.")
                        else:
                            if not valid:
                                print("That move is invalid, please try again!")
                            else:
                                moveFlag = False
                if move != 'q':
                    game.makeMovePlayer(tuple(map(int, move.split())))
        else:
            print("Computer Turn!")
            if game.isGameOver():
                flag = False
            else:
                if difficulty == "1":
                    move = game.makeMoveNaive()
                    print("Computer chooses position:", move)
                else:
                    move = game.makeMoveSmart()
                    print("Computer chooses position:", move)                
                
main()              
        