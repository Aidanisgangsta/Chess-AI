import board 
import game 
import piece_check as pc

import re

whites_move = True

boardstate = list(board.chessboard)

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

def move_vaildator(move: str) -> bool:
    """
    A function that checks if the users move meets the correct format.\n

     - Checks to if the move is 4 characters long.
     - Then checks if the move meets the correct format.
         - Checks if the move contains 2 squares on the board.
    """

    if len(move) == 4:
        # Checks if the move entered is vaild
        valid_move = bool(re.match(r"[a-h][1-8][a-h][1-8]", move))
        if valid_move:
            return True
        else:
            print("Please enter a move in the correct format (e.g. b1c3)")
            return False
    else:
        print("Please enter a valid move")
        return False

def colour_checker(board_location: int) -> bool:
    """
    A function that checks if the piece moved is the correct colour.
    """

    piece: str = boardstate[board_location]

    if whites_move:
        return piece.isupper()
    return piece.islower()

def blank_checker(board_location: int) -> bool:
    """
    A function that checks if the square entered is blank.
    """

    square = boardstate[board_location]

    return square == "."

def move_gen() -> list:
    """
    A function that generates all the possible moves in the position.
    """

    moves = []

    for start_square, piece in enumerate(boardstate):
        if not blank_checker(start_square):
            if colour_checker(start_square):
                for move in piece_moves[piece.casefold()]:
                    # Checks for moves that are more than one square
                    if is_long_distance_piece(piece):
                        for distance in range(1, 9):
                            end_square = start_square + (move * distance)
                            if not whites_move:
                                end_square *= -1
                            if is_valid_move(start_square, end_square):
                                moves.append((start_square, end_square))
                            else:
                                break
                    else:
                        end_square = start_square + move
                        if not whites_move:
                            end_square *= -1
                        if is_valid_move(start_square, end_square):
                            moves.append((start_square, end_square))

    return moves

def is_long_distance_piece(piece: str) -> bool:
    """
    A function that checks if the piece can move more than one square in a specefic direction
    (bishop, queen or rook).
    """

    lwr_piece = piece.casefold()

    if lwr_piece == "b" or lwr_piece == "q" or lwr_piece == "r": 
        return True
    return False

def is_valid_move(start_square: int, end_square: int) -> bool:
    """
    A function that checks if an entered move is legal or not.
    """

    piece_moved = boardstate[start_square].casefold()

    available_moves = piece_moves.get(piece_moved)
    if not whites_move:
        available_moves = [move * -1 for move in available_moves]

    PIECECHECKDICTIONARY = {
        "p": pc.pawn_check, 
        "r": pc.rook_check, 
        "b": pc.bishop_check, 
        "k": pc.king_check,
        "n": pc.knight_check, 
        "q": pc.queen_check
        }

    return PIECECHECKDICTIONARY[piece_moved](start_square, end_square, available_moves, boardstate)
