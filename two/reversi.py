import random as r
import reversiMove as m

class Reversi():
    def __init__(self):
        self.board = []
        self.newGame()
        self.players = {"b":{"player":False, "score":2},"w":{"player":False, "score":2}}
        self.currentPlayer = 0
    
    def newGame(self):
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                if (i == 3 and j == 3) or (i == 4 and j == 4):
                    self.board[i].append("w")
                elif (i==3 and j==4) or (i==4 and j==3):
                    self.board[i].append("b")
                else:
                    self.board[i].append(".")
        
    def getScore(self, colour):
        return self.players[colour]["score"]
    
    def setPlayerColour(self, colour):
        self.players[colour]["player"] = True
        if colour == "b":
            self.players["w"]["player"] = False
        else:
            self.players["b"]["player"] = False
            
    def displayBoard(self):
        print("  ", end="")
        for i in range(8):
            if i != 7:
                print(i, end=" ")
            else:
                print(i)
        for i in range(len(self.board)):
            print(i, end=" ")
            print(" ".join(self.board[i]))
            
    def isPositionValid(self, position, colour, cont=None):
        #check all around, so pos(y)-1->y+1, x-1 to x+1, excluding itself
        assert type(position) is tuple, "Not a tuple"
        assert len(position) == 2, "Not a coordinate"
        assert type(position[0]) is int, "Must be an integer"
        assert type(position[1]) is int, "Must be an integer"
        assert position[0]>=0 and position[0]<=7, "Out of bounds, must be 0-7"
        assert position[1]>=0 and position[1]<=7, "Out of bounds, must be 0-7"
        
        if cont != None:
            if self.board[position[0]][position[1]] == ".":
                return False
            elif self.board[position[0]][position[1]] == colour:
                return True
            else:
                if cont == "up":
                    if position[0] == 0:
                        return False
                    else:
                        return self.isPositionValid((position[0]-1, position[1]), colour, "up")
                        
                elif cont == "down":
                    if position[0] == 7:
                        return False
                    else:
                        return self.isPositionValid((position[0]+1, position[1]), colour, "down")
                        
                elif cont == "left":
                    if position[1] == 0:
                        return False
                    else:
                        return self.isPositionValid((position[0], position[1]-1), colour, "left") 
                        
                elif cont == "lu":
                    if position[0] == 0 or position[1] == 0:
                        return False
                    else:
                        return self.isPositionValid((position[0]-1, position[1]-1), colour, "lu") 
                        
                elif cont == "ru":
                    if position[1] == 7 or position[0] == 0:
                        return False
                    else:
                        return self.isPositionValid((position[0]-1, position[1]+1), colour, "ru")                     
                    
                elif cont == "ld":
                    if position[1] == 0 or position[0] == 7:
                        return False
                    else:
                        return self.isPositionValid((position[0]+1, position[1]-1), colour, "ld") 
                        
                elif cont == "rd":
                    if position[1] == 7 or position[0] == 7:
                        return False
                    else:
                        return self.isPositionValid((position[0]+1, position[1]+1), colour, "rd") 
                        
                else:
                    if position[1] == 7:
                        return False
                    else:
                        return self.isPositionValid((position[0], position[1]+1), colour, "right")
                    
        elif self.board[position[0]][position[1]] == ".":
            #Brand new start, gotta find which way to go
            checkDirection = []
            for i in range(-1,2):
                for j in range(-1,2):
                    if (i!=0 or j!=0) and (position[0]+i>=0 and position[0]+i<=7 and position[1]+j>=0 and position[1]+j<=7):
                        if colour == "b":
                            if self.board[position[0]+i][position[1]+j] == "w":
                                checkDirection.append((position[0]+i, position[1]+j))
                        else:
                            if self.board[position[0]+i][position[1]+j] == "b":
                                checkDirection.append((position[0]+i, position[1]+j))
                                
            print(checkDirection)
            for i in range(len(checkDirection)):
                
                if checkDirection[i][0]<position[0]:
                    print("up")
                    if checkDirection[i][1]==position[1]:
                        return self.isPositionValid(checkDirection[i], colour, "up")
                    elif checkDirection[i][1]==position[1]+1:
                        return self.isPositionValid(checkDirection[i], colour, "ru")
                    else:
                        return self.isPositionValid(checkDirection[i], colour, "lu")
                    
                if checkDirection[i][0]==position[0]:
                    print("left or right")
                    if checkDirection[i][1]==position[1]+1:
                        return self.isPositionValid(checkDirection[i], colour, "right")
                    else:
                        return self.isPositionValid(checkDirection[i], colour, "left")
                    
                else:
                    print("down")
                    if checkDirection[i][1]==position[1]:
                        return self.isPositionValid(checkDirection[i], colour, "down")
                    elif checkDirection[i][1]==position[1]+1:
                        return self.isPositionValid(checkDirection[i], colour, "rd")
                    else:
                        return self.isPositionValid(checkDirection[i], colour, "ld")
        else:
            return False

    def isGameOver(self):
        curPlayer = self.getTurn()
        flag = False
        #if current player cannot make any moves, then the game is over.
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == ".":
                    flag = self.isPositionValid((i,j), curPlayer)
                    if flag:
                        return False
        print("Found Game Over")
        return True
    
    def incrementTurn(self):
        self.currentPlayer = (self.currentPlayer + 1) % 2
        
    def getTurn(self):
        if self.currentPlayer == 0:
            return "b"
        return "w"
    
    def makeMovePlayer(self, position):
        if self.players["b"]["player"]:
            col = "w"
            play = "b"
        else:
            col = "b"
            play = "w"
        dif = m.makeMove(self.board, position, play, col)
        self.players[play]["score"] += dif
        self.players[col]["score"] -= (dif-1)
        self.incrementTurn()

        
        
    def findValidMoves(self, colour):
        positions = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == ".":
                    if self.isPositionValid((i,j), colour):
                        positions.append((i,j))        
        return positions
    
    def makeMoveNaive(self):
        #find all the moves possible, add them to a list, pick one at random
        if self.players["b"]["player"]:
            comp = "w"
            play = "b"
        else:
            comp = "b"
            play = "w"
        positions = self.findValidMoves(comp)
        randChoice = r.randrange(len(positions))
        choice = positions[randChoice]
        dif = m.makeMove(self.board, choice, comp, play)
        self.players[comp]["score"] += dif
        self.players[play]["score"] -= (dif-1)
        self.incrementTurn()
        return choice
        
    def makeMoveSmart(self):
        #find all possible moves, pick the one that will yield the greatest score in this moment (basic smartness)
        if self.players["b"]["player"]:
            comp = "w"
            play = "b"
        else:
            comp = "b"
            play = "w"
        positions = self.findValidMoves(comp)
        maxVal = (0,0) #first is difference, second is index
        score = self.players[comp]["score"]
        #make a copy of the board, play each move see which yields the maximum difference, play that on actual
        for i in range(len(positions)):
            copy = self.board[:]
            dif = m.makeMove(copy, positions[i], comp, play)
            if dif>maxVal[0]:
                maxVal = (dif, i)
        m.makeMove(self.board, positions[maxVal[1]], comp, play)
        self.players[comp]["score"] += dif
        self.players[play]["score"] -= (dif-1)
        self.incrementTurn()
        return positions[maxVal[1]]
