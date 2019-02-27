def makeMove(board, position, colour, anticolour):
    ac = anticolour
    board[position[0]][position[1]] = colour
    scoreDifferential = 0
    #print(positions)
            
    for yDir, xDir in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]: #various directions
        toFlip = []
        h = yDir
        j = xDir
        inFlag = False
        while position[0]+h>=0 and position[0]+h<=7 and position[1]+j>=0 and position[1]+j<=7 and board[position[0]+h][position[1]+j] == ac:
            #print("Found valid next at:", position[0]+h, position[1]+j, "with direction", yDir, xDir)
            toFlip.append((position[0]+h, position[1]+j))
            h += yDir
            j += xDir
            inFlag = True
        #if inFlag:
            #print(board[position[0]+h][position[1]+j])
        if inFlag and position[0]+h>=0 and position[0]+h<=7 and position[1]+j>=0 and position[1]+j<=7 and board[position[0]+h][position[1]+j] == colour:
            scoreDifferential += len(toFlip)
            for x in range(len(toFlip)):
                board[toFlip[x][0]][toFlip[x][1]] = colour            
                   
    #print("Positions to flip:", toFlip)
    return scoreDifferential + 1  