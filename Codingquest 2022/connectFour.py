
#Checks if there's a winning position on a Connect Four game.
def isWinning(board, tile):
    sideLength = len(board)

    #Horizontal Check
    for y in range(sideLength):
        for x in range(sideLength-3): 
            #We'll be subtracting 3 alot because there's no need in checking a horizontal match starting from the (k-2)th index of a k-sized array. (We'd exceed the size if we were to try, and get an error)
            if board[y][x] == tile and board[y][x+1] == tile and board[y][x+2] == tile and board[y][x+3] == tile:
                return True

    #Vertical Check
    for x in range(sideLength):
        for y in range(sideLength-3):
            if board[y][x] == tile and board[y+1][x] == tile and board[y+2][x] == tile and board[y+3][x] == tile:
                return True
    
    #Diagonal to the right Check
    for y in range(sideLength-3):
        for x in range(sideLength-3):
            if board[y][x] == tile and board[y+1][x+1] == tile and board[y+2][x+2] == tile and board[y+3][x+3] == tile:
                return True

    #Diagonal to the left Check
    for y in range(sideLength-3):
        for x in range(sideLength-1, 2, -1): #x = k-1, k-2, ..., 4, 3. x=2 wouldn't make sense, as we would try to reach the -1st index.
            if board[y][x] == tile and board[y+1][x-1] == tile and board[y+2][x-2] == tile and board[y+3][x-3] == tile:
                return True

    return False


# Let each tile represent a player's piece.
# This position is impossible to reach, it's just a demonstration.
# This code helped us solve the fourth question of the competition.
# One improvement would be to make it so that it works for rectangular boards as well. 
example_board = [[0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 1, 1, 0, 0, 0],
                [1, 0, 1, 1, 1, 1],
                [0, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0]]

print("Player 0 winning:" , isWinning(example_board, 0)) #False, no 4 zeros are next to each other
print("Player 1 winning:" , isWinning(example_board, 1)) #True, we have 4 ones both horizontally and vertically matching.

