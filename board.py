import moves

import math

BOARDSIZE = 8

board = (
        "R", "N", "B", "K", "Q", "B", "N", "R",
        "P", "P", "P", "P", "P", "P", "P", "P",
        ".", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".",
        "p", "p", "p", "p", "p", "p", "p", "p",
        "r", "n", "b", "k", "q", "b", "n", "r"
        )

FILE_LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h"]

ROW_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8]

UNICODE_PIECE_SYMBOLS = {
    "R": "♖", "r": "♜",
    "N": "♘", "n": "♞",
    "B": "♗", "b": "♝",
    "Q": "♕", "q": "♛",
    "K": "♔", "k": "♚",
    "P": "♙", "p": "♟",
    ".": "·"
}

def printboard():
    """
    A function that prints the board showing the piece occupying the square with notation printed along the side of the board.\n

     - At the start of every row it prints the row number.
     - At the bottom of every column it prints the column letter.
     - Prints the piece in the square list.
      - If there is no piece, a · will be printed.
      - If there is a piece, the appropriate piece will be printed.
    """

    row_num = BOARDSIZE

    square_num = 0
    for square in board:        
        current_row = BOARDSIZE - math.floor(square_num/BOARDSIZE)
        #Prints the row number for the first row
        if square_num == 0:
            print(row_num, end=' ')
        if row_num == current_row:
            print(f"{UNICODE_PIECE_SYMBOLS.get(square)} ", end =" ")
        else:
            row_num -= 1
            print(f"\n{row_num} {UNICODE_PIECE_SYMBOLS.get(square)} ", end =" ")
        square_num += 1

    #Prints the file letter
    print("\n ", end = " ")
    for i in range(BOARDSIZE):            
        print(f"{FILE_LETTERS[i]} ", end =" ")
    print("")

def main():
    printboard()

if __name__ == '__main__':
    main()