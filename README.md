# Introduction
Chess-AI is a chess engine coded 100% in python using no default chess libraries.

All input data must entered using standard chess notation.

# Features
1. Uses pure python with no chess python libraries.
2. Allows for easy modification of the function of the engine by modifying the vales of individual pieces and pruning values.
3. Takes advantage of 'chess engine tricks' to speed up analysis.
4. Chess-AI allows for castling, en passant, promotion and under-promotion. 

# Limitations
Default Chess-AI does not use tables but can be much stronger with the user of them. 

The functionality and strength of Chess-AI can also be adjusted by modifying the values of pieces and the pruning values. By modifying the pruning values, you can increase the depth at which it can analyse for a sacrafice of missing moves that may be pruned early as they need deep analysis to spot.

# License
Licensed under the [Apache License, Version 2.0 license](LICENSE).
