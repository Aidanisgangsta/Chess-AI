# Introduction
Chess-AI is a chess engine coded 100% in python using no default chess libraries.

# Features
1. Uses pure python with no chess python libraries.
2. Allows for easy modification of the function of the engine by modifying the vales of individual pieces and pruning values.
3. Takes advantage of 'chess engine tricks' to speed up analysis.
4. All input data must entered using standard chess notation.

# Limitations
Chess-AI allows for castling, en passant, promotion and under-promotion. 

Default Chess-AI does not use tables but can be much stronger with the user of them. 
Chess-AI can also be made stronger by modifying the values of pieces and the pruning values. By modifying the pruning values, you can increase the depth at which it can analyse for a sacrafice of missing moves that may be pruned early as they need deep analysis to spot.

# License