BOARDSIZE = 8
board = []

def create_board():
    """
    """
    for x in range(1, BOARDSIZE+1):
        row = []
        for y in range(1, BOARDSIZE+1):
            row.append([x, y, "."])
        board.append(row)

def printannotatedboard():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    rownum = 1
    for row in board:
        print(rownum, end =" ")
        for square in row:
            print(square[2], end =" ")
        rownum += 1
        print("")
    #Prints the file letter
    print(" ", end =" ")
    for i in range(BOARDSIZE):            
        print(f"{letters[i]}", end =" ")

create_board()

printannotatedboard()