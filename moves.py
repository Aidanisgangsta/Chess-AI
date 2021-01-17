import board
import piece_check as pc

import re

#Variable which is 1 when it is whites move and -1 when it is blacks move. 
#Keeps track of whose move it is and gets multiplied by the move value when checking if the move is valid.
#This is so pawn moves are properly tested.
whos_move = 1

move = ""

board_history = []

#Creates a new board as a list
boardstate = list(board.chessboard)

halfmove_checker = 0

N = -10
E = 1
S = 10
W = -1

piece_moves = {
    "p": (N, N+N, N+E, N+W),
    "r": (N, E, S, W),
    "n": (N+N+W, N+N+E, E+E+N, E+E+S, S+S+E, S+S+W, W+W+S, W+W+N),
    "b": (N+W, N+E, S+W, S+E),
    "q": (N, E, S, W, N+W, N+E, S+W, S+E),
    "k": (N, E, S, W, N+W, N+E, S+W, S+E, E+E, W+W)
}

def make_move() -> None:
    """
    Function which a user enters move and it is checked whether it meets the correct format.\n

     - Checks whether the move entered is the correct length (4 characters).
     - Then checks if the move entered fits the correct format.
      - Checks whether the first and third characters of the move entered are between a and h.
      - Check whether the second and fourth characters of the move entered are between 1 and 8.
    """

    while True:
        global move
        global boardstate
        global whos_move

        #Checks if the side is in checkmate or stalemate
        if stalemate():
            print("\nDraw by stalemate")
            break
        if checkmate():
            if whos_move == 1:
                print("Black won by checkmate")
                break
            elif whos_move == -1:
                print("White won by checkmate")
                break

        move = input("\nPlease enter a move: ")
        #Checks whether if it is a valid move
        if len(move) == 4:
            #Checks if move is on the board
            valid_move = bool(re.match(r"[a-h][1-8][a-h][1-8]", move))
            if valid_move:
                valid_move = move_handler()
                if valid_move:
                    print("\nOk, your move has been made\n")
                    #Changes whos move it is
                    whos_move *= -1
                    break
                else:
                    boardstate = list(board.chessboard)
                    print("\nPlease enter a valid move")
            else:
                print("\nPlease enter a move in the correct format (e.g. a1c3)")
        else:
            print("\nPlease enter a move in the correct format (e.g. a1c3)")        

def square_finder(start_square: str, end_square: str) -> tuple:
    """
    A function that finds the value in the board array of the start and end squares for a move.\n

    Returns a tuple containing the array values for the start square and end square for the move.
    """

    #Finds the array position of the starting square
    start_square_letter_value = board.FILE_LETTERS.index(start_square[0]) + 1
    start_square_array_value = 20 + (10 * (8 - int(start_square[1])) + start_square_letter_value)

    #Finds the array position of the ending square
    end_square_letter_value = board.FILE_LETTERS.index(end_square[0]) + 1
    end_square_array_value = 20 + (10 * (8 - int(end_square[1])) + end_square_letter_value)

    return start_square_array_value, end_square_array_value

def blank_checker(array_location: str) -> bool:
    """
    A function that checks whether the enter start square is blank or not.\n

    Returns True or False depending on whether or not the start square is blank.
    """

    start_piece = boardstate[array_location]
    if start_piece == ".":
        return True
    else:
        return False

def colour_checker(array_location: int) -> bool:
    """
    A function which checks if the piece to move is the correct colour.
    """

    piece = boardstate[array_location]

    if whos_move == 1:
        if piece.isupper():
            return True
        else:
            return False
    elif whos_move == -1:
        if piece.islower():
            return True
        else:
            return False

def check_checker(boardstate: list) -> bool:
    """
    A function that takes in a board state and checks if the player is in check.\n

     - Scans over every square in the board and sees if it is occupyed by an opponent piece.
     - If it is, it will see if that piece is attacking the players king.
     - If the king is under attack, it will return a True value otherwise it wil return False.
    """
    
    global whos_move
    
    #Finds location of current colours king 
    king_location = -1
    for i in range(len(boardstate)):
        if whos_move == 1:
            if boardstate[i] == "K":
                king_location = i
        elif whos_move == -1:
            if boardstate[i] == "k":
                king_location = i

    #Iterates over every square in the board
    #Checks if the piece on that sqaure can attack the king
    for i in range(len(boardstate)):
        #Checks if it is whites move
        piece = boardstate[i]
        if whos_move == 1:
            if piece.islower():
                #Checks if the move is a legit move
                whos_move *= -1
                move_check = move_checker(i, king_location, piece)
                whos_move *= -1
                if move_check:
                    return True
        elif whos_move == -1:
            if piece.isupper():
                #Checks if the move is a legit move
                whos_move *= -1
                move_check = move_checker(i, king_location, piece)
                whos_move *= -1
                if move_check:
                    return True
    return False  

def move_checker(array_location, end_array_location, piece_moved) -> bool:
    """
    A function that checks if the piece moved has made a legal move or not.
    """

    #Finds the tuple of available move directions from the dictionary of moves
    available_moves = piece_moves.get(piece_moved.casefold())
    #Total distance moved by the piece in the array
    distance_moved = end_array_location - array_location

    piece_lower = piece_moved.casefold()

    PieceFuncDict = {
        "p": pc.pawn_check, 
        "r": pc.rook_check, 
        "b": pc.bishop_check, 
        "k": pc.king_check,
        "n": pc.knight_check, 
        "q": pc.queen_check
        }

    return PieceFuncDict[piece_lower](int(array_location), end_array_location, available_moves, distance_moved)

def move_handler() -> bool:
    """
    A function that handles and runs all the checks.
    """

    start_square = move[0:2]
    end_square = move[2:4]

    #Gets the array values for the start square and end square for the move
    array_location, end_array_location = square_finder(start_square, end_square)
    #Gets the piece you selected and converts it to lowercase
    piece_moved = board.chessboard[array_location]

    #Finds out if the start square entered is blank
    if blank_checker(array_location):
        return False
    else:
        if move_checker(array_location, end_array_location, piece_moved):

            #Check if the piece entered is the correct colour
            if colour_checker(array_location) == False:
                return False
            
            modify_board(piece_moved, array_location, end_array_location)

            #Checks if a pawn can be promoted
            promotion()

            #Checks if the new board has the players king in check
            if check_checker(boardstate):
                return False
            
            board.chessboard = tuple(boardstate)
            return True
        else:
            return False    

def promotion():
    """
    A function that deals with a pawn that has promoted.
    """

    global boardstate

    if whos_move == 1:
        for i in range(11, 19):
            if boardstate[i] == "P":
                while True:
                    new_piece = input("\nWhat would you like to promote to? ")
                    if new_piece.casefold() in piece_moves:
                        boardstate[i] = new_piece.capitalize()
                        break
                    else:
                        print("\nPlease enter a valid piece (N, B, R, Q)")
    elif whos_move == -1:
        for i in range(91, 99):
            if boardstate[i] == "p":
                while True:
                    new_piece = input("\nWhat would you like to promote to? ")
                    if new_piece.casefold() in piece_moves:
                        boardstate[i] = new_piece.casefold()
                        break
                    else:
                        print("\nPlease enter a valid piece (N, B, R, Q)")

def stalemate():
    """
    A fucntion that checks if the player is in stalemate.
    """

    global whos_move

def checkmate():
    """
    A function that checks if the player is in checkmate.
    """

    unmodified_board = boardstate.copy()

    in_check = check_checker(boardstate)
    
    if in_check:
        pass
    else:
        return False
    print(in_check)

def random_move_gen():
    """
    A function that generates all the moves possible by the pieces.
    """

def threefold_check() -> bool:
    """
    A function that checks if a board state has occured three times.\n

    If it has it will return true which will stop the game and announce a draw.
    If it returns false the game will continue as normal.
    """

    occurances = board_history.count(board_history[-1])
    if occurances == 3:
        return True
    else:
        return False

def modify_board(piece_moved: str, start_square: int, end_square: int) -> None:
    """
    A function that modifies the board to show the move that has been made.\n

     - First finds the piece that was moved.
     - A new board object is created as a list.
     - The appropriate squares are replaced.
     - The old board is added to a list containing all the previous board positions.
     - The board is set to = the new board as a tuple.
    """

    global boardstate
    #Replaces pieces old location with a blank square
    boardstate[start_square] = "."
    #Replaces the old square with the new piece
    boardstate[end_square] = piece_moved