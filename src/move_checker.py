import board 
import game 
import piece_check as pc

import re

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