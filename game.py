import board
import moves
import chess_ai

halfmove_checker = 0

def main():
    board.printboard()
    while True:
        moves.make_move()
        global halfmove_checker
        halfmove_checker += 1

        #Checks for threefold repition
        if threefold_check():
            print("\nDraw by threefold repition")
            break
        
        #Checks for 50 move rule
        if halfmove_checker == 99:
            print("\nDraw by 50 move rule")
            break

main()