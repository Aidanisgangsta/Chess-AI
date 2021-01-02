from board import chessboard
from moves import whos_move, piece_moves, move_checker
from random import choice

#Piece-value tables and piece values
piece_values = {"p": 100, "n": 310, "b": 330, "r": 500, "q": 900, "k": 20000}

#Piece-Square Tables
piece_square_tables = {
    "p": (0,  0,  0,  0,  0,  0,  0,  0,
        50, 50, 50, 50, 50, 50, 50, 50,
        10, 10, 20, 30, 30, 20, 10, 10,
        5,  5, 10, 25, 25, 10,  5,  5,
        0,  0,  0, 20, 20,  0,  0,  0,
        5, -5,-10,  0,  0,-10, -5,  5,
        5, 10, 10,-20,-20, 10, 10,  5,
        0,  0,  0,  0,  0,  0,  0,  0),

    "n": (-50,-40,-30,-30,-30,-30,-40,-50,
        -40,-20,  0,  0,  0,  0,-20,-40,
        -30,  0, 10, 15, 15, 10,  0,-30,
        -30,  5, 15, 20, 20, 15,  5,-30,
        -30,  0, 15, 20, 20, 15,  0,-30,
        -30,  5, 10, 15, 15, 10,  5,-30,
        -40,-20,  0,  5,  5,  0,-20,-40,
        -50,-40,-30,-30,-30,-30,-40,-50),

    "b": (-20,-10,-10,-10,-10,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5, 10, 10,  5,  0,-10,
        -10,  5,  5, 10, 10,  5,  5,-10,
        -10,  0, 10, 10, 10, 10,  0,-10,
        -10, 10, 10, 10, 10, 10, 10,-10,
        -10,  5,  0,  0,  0,  0,  5,-10,
        -20,-10,-10,-10,-10,-10,-10,-20),

    "r": (0,  0,  0,  0,  0,  0,  0,  0,
        5, 10, 10, 10, 10, 10, 10,  5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        0,  0,  0,  5,  5,  0,  0,  0),

    "q": (0,  0,  0,  0,  0,  0,  0,  0,
        5, 10, 10, 10, 10, 10, 10,  5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        0,  0,  0,  5,  5,  0,  0,  0),

    "k": (-30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -20,-30,-30,-40,-40,-30,-30,-20,
        -10,-20,-20,-20,-20,-20,-20,-10,
        20, 20,  0,  0,  0,  0, 20, 20,
        20, 30, 10,  0,  0, 10, 30, 20)
}


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

if __name__ == "__main__":
    random_move_gen()