import reversi
def main():
    #create new instance of the game reversi
    game = reversi.Reversi()
    #print out starting information and get the colour of the player
    print("Starting new game!")
    print("Black goes first, then white")
    playColour = input("Enter 'b' to play black, 'w' to choose white: ")
    #ensure player chooses a valid colour
    while playColour != "b" and playColour != "w":
            playColour = input("Enter 'b' to play black, 'w' to choose white: ")
    game.setPlayerColour(playColour)
    #ensure player chooses a  valid computer opponent difficulty
    difficulty = input("Enter '1' to choose easy computer opponent, '2' for hard computer opponent: ")
    while difficulty != "1" and difficulty != "2":
        difficulty = input("Enter '1' to choose easy computer opponent, '2' for hard computer opponent: ")
    #create the main game loop
    flag = True
    while flag:
        #display the current status of the game and score
        game.displayBoard()
        print("Score: white %d, black %d" % (game.getScore("w"), game.getScore("b")))
        #check game over
        if game.isGameOver():
            flag = False
        #check if its the players turn
        elif game.getTurn() == playColour:
            #players turn, get input for what they want.
            moveFlag = True
            while moveFlag:
                move = input("Enter 2 numbers from 0-7 separated by a space to make a move, where the first number is the row and the second number is the column\nEnter 'q' to quit or 'h' for help.->")
                if move == 'q':
                    #set all the flags to be False, exiting the game
                    flag = False
                    moveFlag = False
                elif move == "h":
                    #call the help function on the instance of game (shows all possible moves)
                    game.help()
                else:
                    try:
                        #validate the move
                        valid = game.isPositionValid(tuple(map(int, move.split())), playColour)
                    except AssertionError as a:
                        #if the asserts failed in isPositionValid this is returned
                        print("Invalid position: ", a.args[0])
                    except TypeError:
                        #If the person failed to pass integers this is caught
                        print("You need to enter an integer between 0 and 7 for each coordinate.")
                    else:
                        #the actual position was valid
                        if not valid:
                            #but it's not an appropriate move
                            print("Invalid position: piece doesn't surround line of opponent pieces.")
                        else:
                            #we found our move
                            moveFlag = False
            if move != 'q':
                #if we weren't exiting, make the move
                game.makeMovePlayer(tuple(map(int, move.split())))
        else:
            #computers turn!
            if difficulty == "1":
                move = game.makeMoveNaive()
                print("Computer making move:", move)
            else:
                move = game.makeMoveSmart()
                print("Computer making move:", move)                

#big big loop that is responsible for playing multiple games
mainFlag = True
while mainFlag:
    #calls a new game
    main() 
    #asking if they would like to play again
    resp = input("Would you like to play again?(y/n): ")
    #validate
    while resp!="y" and resp!="n":
        resp = input("Would you like to play again?(y/n): ")
    #exiting if not
    if resp == "n":
        mainFlag = False
        