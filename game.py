import board
import moves
import chess_ai

def threefold_check() -> bool:
    """
    A function that checks if a board state has occured three times.\n

    If it has it will return true which will stop the game and announce a draw.
    If it returns false the game will continue as normal.
    """

    for board in moves.board_history:
        occurances = moves.board_history.count(board)
        print(occurances)
        if occurances == 3:
            return True
        else:
            return False

def main():
    board.printboard()
    while True:
        moves.main()
        #Checks for threefold repition
        if threefold_check():
            print("\nDraw by threefold repition")
            break

main()