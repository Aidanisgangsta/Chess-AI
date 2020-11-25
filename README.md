# Introduction
Chess-AI is a chess engine coded 100% in python using no default chess libraries.

All input data (moves) is entered in a format where the first 2 character are the square which the piece you want to move is currently on and the last 2 characters are the square that you want to move the piece to (e.g. b1c3).

# Features
1. Uses pure python with no chess python libraries.
2. Allows for easy modification of the function of the engine by modifying the vales of individual pieces and pruning values.
3. Takes advantage of 'chess engine tricks' to speed up analysis.
4. Chess-AI allows for castling, en passant, promotion and under-promotion. 

# Entering moves
Moves are entered into Chess-AI in a 4 digit format.

The fist 2 digits are the coordinates of the piece you would like to move.

The last 2 digits are the coordinates of the square you would like the piece to move to.

Examples: b1c3 (Nc3 in starting position), d2d4 (d4 in starting position), e1g1 (Short castles assuming it is possible)

# Limitations
Default Chess-AI does not use tables but can be much stronger with the user of them. 

The functionality and strength of Chess-AI can also be adjusted by modifying the values of pieces and the pruning values. By modifying the pruning values, you can increase the depth at which it can analyse for a sacrafice of missing moves that may be pruned early as they need deep analysis to spot.

# License
Licensed under the [Apache License, Version 2.0 license](LICENSE).
