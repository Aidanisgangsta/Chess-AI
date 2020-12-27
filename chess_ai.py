from board import chessboard
from moves import whos_move, piece_moves, move_checker
from random import choice

#Piece-value tables and piece values
piece_values = {"p": 100, "n": 300, "b": 320, "r": 510, "q": 900, "k": 999999}

def random_move_gen():
    moves = []
    #Finds all the possible moves for the player
    for i in range(len(chessboard)):
        if whos_move == 1:
            if chessboard[i].isupper():
                for move in piece_moves[chessboard[i].casefold()]:
                    moves.append((i, i + (move * whos_move), chessboard[i]))
        elif whos_move == -1:
            if chessboard[i].islower():
                for move in piece_moves[chessboard[i].casefold()]:
                    moves.append((i, i + (move * whos_move), chessboard[i]))
    while True:
        rnd_move = choice(moves)
        move_checker(rnd_move[0], rnd_move[1], rnd_move[2])

random_move_gen()