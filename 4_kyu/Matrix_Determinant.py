# Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.

from numpy.linalg import det
import numpy as np

def determinant(matrix):
    return matrix[0][0] if len(matrix)==1 else int(round(det(np.array(matrix))))
