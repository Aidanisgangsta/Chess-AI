import board
import moves
import chess_ai as ai

def game():
    while True:
        moves.board_history.append(board.chessboard)
        board.printboard(board.chessboard)
        moves.make_move()
        moves.halfmove_checker += 1

        #Checks for threefold repition
        if moves.threefold_check():
            print("\nDraw by threefold repitition")
            break
        
        #Checks for 50 move rule
        if moves.halfmove_checker == 99:
            print("\nDraw by 50 move rule")
            break

if __name__ == "__main__":
    game()