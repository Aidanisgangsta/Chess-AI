from board import chessboard
from moves import whos_move, piece_moves, move_checker
from random import choice

#Piece-value tables and piece values
piece_values = {"p": 100, "n": 300, "b": 320, "r": 510, "q": 900, "k": 999999}

def random_move_gen():
    moves = []
    #Finds all the possible moves for the player
    for i, square in enumerate(chessboard):
        if whos_move == 1:
            if square.isupper():
                for move in piece_moves[square.casefold()]:
                    if square == "R" or square == "B" or square == "Q":
                        for d in range(1, 9):
                            end_square = i + (move * whos_move * d)
                            if end_square < 0 or end_square > 119:
                                continue
                            else:
                                moves.append((i, end_square, square))
                    else:
                        end_square = i + (move * whos_move)
                        if end_square < 0 or end_square > 119:
                            continue
                        else:
                            moves.append((i, end_square, square))

        elif whos_move == -1:
            if chessboard[i].islower():
                for move in piece_moves[chessboard[i].casefold()]:
                    moves.append((i, i + (move * whos_move), chessboard[i]))
    print(moves)
    while True:
        rnd_move = choice(moves)
        move_checker(rnd_move[0], rnd_move[1], rnd_move[2])

random_move_gen()