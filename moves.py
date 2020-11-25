import board

import re

board_history = []

N = -8
E = 1
S = 8
W = -1

moves = {
    "p": (N, N+N, N+E, N+W),
    "r": (N, E, S, W),
    "n": (N+N+W, N+N+E, E+E+N, E+E+S, S+S+E, S+S+W, W+W+S, W+W+N),
    "b": (N+W, N+E, S+W, S+E),
    "q": (N, E, S, W, N+W, N+E, S+W, S+E),
    "k": (N, E, S, W, N+W, N+E, S+W, S+E)
}

def make_move():
    """
    Function which a user enters move and it is checked whether it meets the correct format.\n

     - Checks whether the move entered is the correct length (4 characters).
     - Then checks if the move entered fits the correct format.
      - Checks whether the first and third characters of the move entered are between a and h.
      - Check whether the second and fourth characters of the move entered are between 1 and 8.
    """

    while True:
        move = input("\nPlease enter a move: ")
        #Checks whether if it is a valid move
        if len(move) == 4:
            #Checks if move is on the board
            valid_move = bool(re.match(r"[a-h][1-8][a-h][1-8]", move))
            if valid_move == True:
                valid_move = move_checker(move)
                if valid_move == True:
                    print("\nOk, your move has been made\n")
                    board.printboard()
            else:
                print("\nPlease enter a move in the correct format (e.g. a1c3)")
        else:
            print("\nPlease enter a move in the correct format (e.g. a1c3)")

def move_checker(move: str) -> bool:
    start_square = move[0:2]
    end_square = move[2:4]

    def square_finder() -> tuple:
        """
        A function that finds the value in the board array of the start and end squares for a move.\n

        Returns a tuple containing the array values for the start square and end square for the move.
        """

        #Finds the array position of the starting square
        start_square_letter_value = board.FILE_LETTERS.index(start_square[0])
        start_square_array_value = 8 * (8 - int(start_square[1])) + start_square_letter_value

        #Finds the array position of the ending square
        end_square_letter_value = board.FILE_LETTERS.index(end_square[0])
        end_square_array_value = 8 * (8 - int(end_square[1])) + end_square_letter_value

        return start_square_array_value, end_square_array_value

    def blank_checker() -> bool:
        """
        A function that checks whether the enter start square is blank or not.\n

        Returns True or False depending on whether or not the start square is blank.
        """

        start_piece = board.board[array_values[0]]

        if start_piece == ".": 
            print("\nPlease enter a location which is not blank")
            return True
        else:
            return False

    def legit_move_checker() -> bool:
        """
        A function that finds out if a move entered is a legitimate move according to the piece.\n
        """

        #Gets the location in the array of the starting position of the piece
        array_location = array_values[0]
        #Gets the array locatoin of the end square of the piece
        end_array_location = array_values[1]
        #Gets the piece you selected and converts it to lowercase
        piece_moved = (board.board[array_location]).casefold()
        #Gets the dictionary of move values from the moves module
        piece_moves_dict = moves
        #Finds the tuple of available moves from the dictionary of moves
        available_moves = piece_moves_dict.get(piece_moved)

        def pawn_check() -> bool:
            """
            A function that checks if a pawn move is possible
            """

            #Iterates over every possible pawn move
            for move in available_moves:
                #Checks if the start location + the change is direction by the move in the array = end location
                if array_location + move == end_array_location:
                    #Checks if the move is a move straight forward and the squares are clear
                    if move % 8 == 0 and board.board[end_array_location] == ".":
                        return True
                    else:
                        #Checks if the move is a possible capture
                        piece_to_capture = board.board[end_array_location]
                        if piece_to_capture.isupper():
                            return True
            return False

        def rook_check():
            pass

        def bishop_check():
            pass

        def king_check():
            pass

        def knight_check():
            pass

        def queen_check():
            pass

        if piece_moved == "p":
            legit_move = pawn_check()
            if legit_move == True:
                return True
            else: 
                return False
        elif piece_moved == "r":
            rook_check()
        elif piece_moved == "b":
            bishop_check()
        elif piece_moved == "k":
            king_check()
        elif piece_moved == "n":
            knight_check()
        elif piece_moved == "q":
            queen_check()
    
    #Gets a tuple containing the array values for the start square and end square for the move
    array_values = square_finder()
    #Finds out if the start square entered is blank
    is_blank = blank_checker()
    #Checks if square is blank
    if is_blank == True:
        return False
    #Checks if the move entered is a valid move by that piece
    legit_move = legit_move_checker()

    if legit_move == True:
        modify_board(array_values)
        return True
    else:
        return False

def modify_board(array_values: tuple):
    """
    A function that modifies the board to show the move that has been made.\n

     - First finds the piece that was moved.
     - A new board object is created as a list.
     - The appropriate squares are replaced.
     - The old board is added to a list containing all the previous board positions.
     - The board is set to = the new board as a tuple.
    """

    #Find the piece that was moved
    piece_moved = (board.board[array_values[0]]).casefold()
    #Creates new board object
    new_board = list(board.board)
    #Replaces pieces old location with a blank square
    new_board[array_values[0]] = "."
    #Replaces the old square with the new piece
    new_board[array_values[1]] = piece_moved

    #Appends the old board to a list of all the board positions
    board_history.append(board.board)
    board.board = tuple(new_board)

def main():
    board.printboard()
    make_move()

if __name__ == '__main__':
    main()