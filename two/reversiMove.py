def makeMove(board, position, colour, anticolour):
    ac = anticolour
    positions = []
    board[position[0]][position[1]] = colour
    for i in range(-1,2):
        for j in range(-1,2):
            if (i!=0 or j!=0):
                #print(position)
                if (position[0]+i>=0 and position[0]+i<=7 and position[1]+j>=0 and position[1]+j<=7) and board[position[0]+i][position[1]+j] == ac:
                    positions.append((position[0]+i, position[1]+j))
    
    #check each direction where we're going if its good and has something on the other end
    scoreDifferential = 0
    print(positions)
    for i in range(len(positions)):
        toFlip = []        
        if positions[i][0]<position[0]:
            h = 0
            j = 0
            print("goes up")
            if positions[i][1]==position[1]:
                #up only
                while board[positions[i][0]+h][positions[i][1]] == ac and positions[i][0]+h>0:
                    toFlip.append((positions[i][0]+h, positions[i][1]+j))
                    h -= 1
                if board[positions[i][0]+h][positions[i][1]+j] == colour:
                    scoreDifferential += len(toFlip)
                    for x in range(len(toFlip)):
                        board[toFlip[x][0]][toFlip[x][1]] = colour
                        
            elif positions[i][1]==position[1]+1:
                #up and right
                while board[positions[i][0]+h][positions[i][1]+j] == ac and positions[i][0]+h>0 and positions[i][1]+j<7:
                    toFlip.append((positions[i][0]+h, positions[i][1]+j))
                    j += 1
                    h -= 1
                if board[positions[i][0]+h][positions[i][1]+j] == colour:
                    scoreDifferential += len(toFlip)
                    for x in range(len(toFlip)):
                        board[toFlip[x][0]][toFlip[x][1]] = colour
                        
            else:
                #up and left
                while board[positions[i][0]+h][positions[i][1]+j] == ac and positions[i][0]+h>0 and positions[i][1]+j>0:
                    toFlip.append((positions[i][0]+h, positions[i][1]+j))
                    j -= 1
                    h -= 1
                if board[positions[i][0]+h][positions[i][1]+j] == colour:
                    scoreDifferential += len(toFlip)
                    for x in range(len(toFlip)):
                        board[toFlip[x][0]][toFlip[x][1]] = colour    
                            
                        
        if positions[i][0]==position[0]:
            print("goes left right")
            h = 0
            j = 0
            if positions[i][1]==position[1]+1:
                while board[positions[i][0]+h][positions[i][1]+j] == ac and positions[i][1]+j<7:
                    toFlip.append((positions[i][0]+h, positions[i][1]+j))
                    j += 1
                if board[positions[i][0]+h][positions[i][1]+j] == colour:
                    scoreDifferential += len(toFlip)
                    for x in range(len(toFlip)):
                        board[toFlip[x][0]][toFlip[x][1]] = colour
                        
            else:
                while board[positions[i][0]+h][positions[i][1]+j] == ac and positions[i][1]+j>0:
                    toFlip.append((positions[i][0]+h, positions[i][1]+j))
                    j -= 1
                if board[positions[i][0]+h][positions[i][1]+j] == colour:
                    scoreDifferential += len(toFlip)
                    for x in range(len(toFlip)):
                        board[toFlip[x][0]][toFlip[x][1]] = colour
            
            
        else:
            print("goes down")
            h = 0
            j = 0
            if positions[i][1]==position[1]:
                print("goes exclusively down")
                print("In position underneath")
                while board[positions[i][0]+h][positions[i][1]] == ac and positions[i][0]+h<7:
                    print("add it in")
                    toFlip.append((positions[i][0]+h, positions[i][1]+j))
                    h+=1
                if board[positions[i][0]+h][positions[i][1]] == colour:
                    scoreDifferential += len(toFlip)
                    for x in range(len(toFlip)):
                        board[toFlip[x][0]][toFlip[x][1]] = colour
                        
            elif positions[i][1]==position[1]+1:
                print("goes down and to the right")
                while board[positions[i][0]+h][positions[i][1]+j] == ac and positions[i][0]+h<7 and positions[i][1]+j<7:
                    toFlip.append((positions[i][0]+h, positions[i][1]+j))
                    j += 1
                    h+=1
                if board[positions[i][0]+h][positions[i][1]+j] == colour:
                    scoreDifferential += len(toFlip)
                    for x in range(len(toFlip)):
                        board[toFlip[x][0]][toFlip[x][1]] = colour
            else:
                print("goes down and to the left")
                while board[positions[i][0]+h][positions[i][1]+j] == ac and positions[i][0]+h<7 and positions[i][1]+j>0:
                    toFlip.append((positions[i][0]+h, positions[i][1]+j))
                    j -= 1
                    h+=1
                if board[positions[i][0]+h][positions[i][1]+j] == colour:
                    scoreDifferential += len(toFlip)
                    for x in range(len(toFlip)):
                        board[toFlip[x][0]][toFlip[x][1]] = colour       
    print("Positions to flip:", toFlip)
    return scoreDifferential + 1  