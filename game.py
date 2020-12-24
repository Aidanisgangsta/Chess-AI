from board import printboard, chessboard
import moves

def game():
    while True:
        printboard(chessboard)
        moves.make_move()
        moves.halfmove_checker += 1

        #Checks for threefold repition
        if moves.threefold_check():
            print("\nDraw by threefold repition")
            break
        
        #Checks for 50 move rule
        if moves.halfmove_checker == 99:
            print("\nDraw by 50 move rule")
            break

if __name__ == "__main__":
    game()