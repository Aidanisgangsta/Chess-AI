import moves as m
import board

def pawn_check(array_location, end_array_location, available_moves) -> bool:
    """
    A function that checks if a pawn move is possible
    """

    #Iterates over every possible pawn move
    for move in available_moves:
        #Checks if the start location + the change is direction by the move in the array = end location
        if array_location + (move * m.whos_move) == end_array_location:
            #Checks if the move is a move straight forward and the squares are clear
            if (move * m.whos_move) % 8 == 0 and m.boardstate[end_array_location] == ".":
                #Checks if the move is 2 squares forward
                if move == -16:
                    #Checks the square 1 square ahead of the pawn
                    if m.boardstate[array_location + (m.whos_move * -8)] == ".":
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                #Checks if the move is a possible capture
                piece_to_capture = m.boardstate[end_array_location]
                if m.whos_move == 1:
                    if piece_to_capture.islower():
                        return True
                elif m.whos_move == -1:
                    if piece_to_capture.isupper():
                        return True

            #Checks for en passant capture
            if piece_to_capture == ".":
                if m.whos_move == 1:
                    if m.boardstate[end_array_location + 8] == "p":
                        if m.board_history[-2][end_array_location - 8] == "p" and m.board_history[-2][end_array_location + 8] == ".":
                            m.boardstate[end_array_location + 8] = "."
                            return True
                        else:
                            return False
                    else:
                        return False
                elif m.whos_move == -1:
                    if m.boardstate[end_array_location - 8] == "P":
                        if m.board_history[-2][end_array_location - 8] == "p" and m.board_history[-2][end_array_location + 8] == ".":
                            m.boardstate[end_array_location - 8] = "."
                            return True
    return False

def rook_check(array_location, available_moves, distance_moved) -> bool:
    """
    A function that checks if a rook move is possible
    """

    #Iterates over every possible rook move
    for move in available_moves:
        #Iterates over all the rows the rook can possibly move on
        for i in range(1, board.BOARDSIZE):
            #Checks to see if the index is within the tuple
            if (array_location + (i * move)) < 64 and (array_location + (i * move)) > -1:
                #Checks if every square along the row is blank or if the end square can be captured
                if m.boardstate[array_location + (i * move)] == ".":
                    #Checks if the start location + the change is direction by the move in the array = end location
                    if i * move == distance_moved:
                        return True
                #Checks if the move is a possible capture
                elif m.whos_move == 1:
                    if m.boardstate[array_location + (i * move)].islower():
                        if i * move == distance_moved:
                            return True
                        else:
                            break
                elif m.whos_move == -1:
                    if m.boardstate[array_location + (i * move)].isupper():
                        if i * move == distance_moved:
                            return True
                        else:
                            break
                else:
                    break
    return False

def bishop_check(array_location, available_moves, distance_moved) -> bool:
    """
    A function that checks if a bishop move is possible
    """

    #Iterates over every possible bishop move
    for move in available_moves:
        #Iterates over all the diagonals the bishop can possibly move on
        for i in range(1, board.BOARDSIZE):
            #Checks to see if the index is within the tuple
            if (array_location + (i * move)) < 64 and (array_location + (i * move)) > -1:
                #Checks if every square along the diagonal is blank or if the end square can be captured
                if m.boardstate[array_location + (i * move)] == ".":
                    #Checks if the start location + the change is direction by the move in the array = end location
                    if i * move == distance_moved:
                        return True
                #Checks if the move is a possible capture
                elif m.whos_move == 1:
                    if m.boardstate[array_location + (i * move)].islower():
                        if i * move == distance_moved:
                            return True
                        else:
                            break
                elif m.whos_move == -1:
                    if m.boardstate[array_location + (i * move)].isupper():
                        if i * move == distance_moved:
                            return True
                        else:
                            break
                else:
                    break
    return False

def king_check(array_location, end_array_location, available_moves) -> bool:
    """
    A function that checks if a king move is possible
    """

    #Iterates over every possible king move
    for move in available_moves:
        #Checks if the start location + the change is direction by the move in the array = end location
        if array_location + move == end_array_location:
            #Checks if the move lands on a clear square
            if m.boardstate[end_array_location] == ".":
                return True
            else:
                #Checks if the move is a possible capture
                piece_to_capture = m.boardstate[end_array_location]
                if m.whos_move == 1:
                    if piece_to_capture.islower():
                        return True
                elif m.whos_move == -1:
                    if piece_to_capture.isupper():
                            return True
                else:
                    return False
    return False

def knight_check(array_location, end_array_location, available_moves) -> bool:
    """
    A function that checks if a knight move is possible.
    """

    #Iterates over all possible knight moves
    for move in available_moves:
        #Checks if the start location + the change in location by the move = end location
        if array_location + move == end_array_location:
            #Checks if the move lands on a clear square
            if m.boardstate[end_array_location] == ".":
                return True
            else:
                piece_to_capture = m.boardstate[end_array_location]
                if m.whos_move == 1:
                    if piece_to_capture.islower():
                        return True
                elif m.whos_move == -1:
                    if piece_to_capture.isupper():
                        return True
                else:
                    return False
    return False

def queen_check(array_location, available_moves, distance_moved) -> bool:
    """
    A function that checks if a queen move is possible
    """

    #Iterates over every possible queen move
    for move in available_moves:
        #Iterates over all the diagonals and rows the queen can possibly move on
        for i in range(1, board.BOARDSIZE):
            #Checks to see if the index is within the tuple
            if (array_location + (i * move)) < 64 and (array_location + (i * move)) > -1:
                #Checks if every square along the row is blank or if the end square can be captured
                if m.boardstate[array_location + (i * move)] == ".":
                    #Checks if the start location + the change is direction by the move in the array = end location
                    if i * move == distance_moved:
                        return True
                #Checks if the move is a possible capture
                elif m.whos_move == 1:
                    if m.boardstate[array_location + (i * move)].islower():
                        if i * move == distance_moved:
                            return True
                        else:
                            break
                elif m.whos_move == -1:
                    if m.boardstate[array_location + (i * move)].isupper():
                        if i * move == distance_moved:
                            return True
                        else:
                            break
                else:
                    break 
    return False