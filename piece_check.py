import moves
import board

#Gets the array values for the start square and end square for the move
array_location, end_array_location = moves.square_finder()
#Gets the piece you selected and converts it to lowercase
piece_moved = moves.boardstate[array_location]
#Finds the tuple of available moves from the dictionary of moves
available_moves = moves.piece_moves.get(piece_moved.casefold())
#Total distance moved by the piece in the array
distance_moved = end_array_location - array_location

def pawn_check() -> bool:
    """
    A function that checks if a pawn move is possible
    """

    print(moves.whos_move)

    #Iterates over every possible pawn move
    for move in available_moves:
        #Checks if the start location + the change is direction by the move in the array = end location
        if array_location + (move * moves.whos_move) == end_array_location:
            #Checks if the move is a move straight forward and the squares are clear
            if (move * moves.whos_move) % 8 == 0 and moves.boardstate[end_array_location] == ".":
                #Checks if the move is 2 squares forward
                if move == -16:
                    #Checks the square 1 square ahead of the pawn
                    if moves.boardstate[array_location + (moves.whos_move * -8)] == ".":
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                #Checks if the move is a possible capture
                piece_to_capture = moves.boardstate[end_array_location]
                if moves.whos_move == 1:
                    if piece_to_capture.islower():
                        return True
                elif moves.whos_move == -1:
                    if piece_to_capture.isupper():
                        return True

            new_board = list(moves.boardstate)
            #Checks for en passant capture
            if piece_to_capture == ".":
                if moves.whos_move == 1:
                    if moves.boardstate[end_array_location + 8] == "p":
                        if moves.board_history[-1][end_array_location - 8] == "p" and moves.board_history[-1][end_array_location + 8] == ".":
                            new_board[end_array_location + 8] = "."
                            return True
                        else:
                            return False
                    else:
                        return False
                elif moves.whos_move == -1:
                    if moves.boardstate[end_array_location - 8] == "P":
                        if moves.board_history[-1][end_array_location - 8] == "p" and moves.board_history[-1][end_array_location + 8] == ".":
                            new_board[end_array_location - 8] = "."
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                return False

def rook_check() -> bool:
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
                if moves.boardstate[array_location + (i * move)] == ".":
                    #Checks if the start location + the change is direction by the move in the array = end location
                    if i * move == distance_moved:
                        return True
                #Checks if the move is a possible capture
                elif moves.whos_move == 1:
                    if moves.boardstate[array_location + (i * move)].islower():
                        if i * move == distance_moved:
                            return True
                        else:
                            break
                elif moves.whos_move == -1:
                    if moves.boardstate[array_location + (i * move)].isupper():
                        if i * move == distance_moved:
                            return True
                        else:
                            break
                else:
                    break
    return False

def bishop_check() -> bool:
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
                if moves.boardstate[array_location + (i * move)] == ".":
                    #Checks if the start location + the change is direction by the move in the array = end location
                    if i * move == distance_moved:
                        return True
                #Checks if the move is a possible capture
                elif moves.whos_move == 1:
                    if moves.boardstate[array_location + (i * move)].islower():
                        if i * move == distance_moved:
                            return True
                        else:
                            break
                elif moves.whos_move == -1:
                    if moves.boardstate[array_location + (i * move)].isupper():
                        if i * move == distance_moved:
                            return True
                        else:
                            break
                else:
                    break
    return False

def king_check() -> bool:
    """
    A function that checks if a king move is possible
    """

    #Iterates over every possible king move
    for move in available_moves:
        #Checks if the start location + the change is direction by the move in the array = end location
        if array_location + move == end_array_location:
            #Checks if the move lands on a clear square
            if moves.boardstate[end_array_location] == ".":
                return True
            else:
                #Checks if the move is a possible capture
                piece_to_capture = moves.boardstate[end_array_location]
                if moves.whos_move == 1:
                    if piece_to_capture.islower():
                        return True
                elif moves.whos_move == -1:
                    if piece_to_capture.isupper():
                            return True
                else:
                    return False
    return False

def knight_check() -> bool:
    """
    A function that checks if a knight move is possible.
    """

    #Iterates over all possible knight moves
    for move in available_moves:
        #Checks if the start location + the change in location by the move = end location
        if array_location + move == end_array_location:
            #Checks if the move lands on a clear square
            if moves.boardstate[end_array_location] == ".":
                return True
            else:
                piece_to_capture = moves.boardstate[end_array_location]
                if moves.whos_move == 1:
                    if piece_to_capture.islower():
                        return True
                elif moves.whos_move == -1:
                    if piece_to_capture.isupper():
                        return True
                else:
                    return False
    return False

def queen_check() -> bool:
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
                if moves.boardstate[array_location + (i * move)] == ".":
                    #Checks if the start location + the change is direction by the move in the array = end location
                    if i * move == distance_moved:
                        return True
                #Checks if the move is a possible capture
                elif moves.whos_move == 1:
                    if moves.boardstate[array_location + (i * move)].islower():
                        if i * move == distance_moved:
                            return True
                        else:
                            break
                elif moves.whos_move == -1:
                    if moves.boardstate[array_location + (i * move)].isupper():
                        if i * move == distance_moved:
                            return True
                        else:
                            break
                else:
                    break 
    return False

def main():
    #Checks if the move entered is a valid move by that piece
    if moves.legit_move_checker():
        #Checks if the players king is in check
        if moves.modify_board(array_location, end_array_location) == False:
            return False
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    main()