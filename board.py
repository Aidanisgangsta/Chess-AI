BOARDSIZE = 8
board = []

def create_board():
    """
    A function that creates the board object.\n

    Creates a 8x8 grid of list which contain the x and y coordinates as well as the piece occupying the square.
    """

    for x in range(1, BOARDSIZE+1):
        row = []
        for y in range(1, BOARDSIZE+1):
            row.append([x, y, "."])
        board.append(row)

def printannotatedboard():
    """
    A function that prints the board showing the piece occupying the square with notation printed along the side of the board.\n

     - At the start of every row it prints the row number.
     - At the bottom of every column it prints the column letter.
     - Prints the 3rd item (piece) in the square list.
    """

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