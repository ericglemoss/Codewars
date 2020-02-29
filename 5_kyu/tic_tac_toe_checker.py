# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? 
# Our goal is to create a function that will check that for us!

# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 
# 1 if it is an "X", or 2 if it is an "O".

# We want our function to return:
# -1 if the board is not yet finished (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.


import numpy as np
def is_solved(board):
    board = np.array(board)
    for i in range(3):
        if np.all(board[i,:] == 1):
            return 1
        elif np.all(board[i,:] == 2):
            return 2
    for j in range(3):
        if np.all(board[:,j] == 1):
            return 1
        elif np.all(board[:,j] == 2):
            return 2
    if np.all(board.diagonal() == 1):
        return 1
    elif np.all(board.diagonal() == 2):
        return 2
    elif np.all(np.fliplr(board).diagonal() == 1):
        return 1
    elif np.all(np.fliplr(board).diagonal() == 2):
        return 2
    elif 0 in board:
        return -1
    else:
        return 0
