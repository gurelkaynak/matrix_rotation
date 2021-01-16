#!/bin/python

import math
import os
import random
import re
import sys

        
# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    matrix_m = len(matrix)
    matrix_n = len(matrix[0])
    
    if matrix_m < matrix_n:
        layers = matrix_m / 2
    else:
        layers = matrix_n / 2 
        
    for layer in range(layers):
        matrix_m1 = matrix_m - 2 * layer
        matrix_n1 = matrix_n - 2 * layer
        optimized_rotations = r % (2 * matrix_m1 + 2 * (matrix_n1 - 2))
        rotations = 0
        while rotations < optimized_rotations:
            rotations += 1
            current_value = matrix[layer][layer]
            # Go south
            for i in range(layer + 1, matrix_m - layer):
                tmp_value = current_value
                current_value = matrix[i][layer]
                matrix[i][layer] = tmp_value
            # Go east
            for j in range(layer + 1, matrix_n - layer):
                tmp_value = current_value
                current_value = matrix[matrix_m - layer - 1][j]
                matrix[matrix_m - layer - 1][j] = tmp_value
            # Go north
            for i in range(matrix_m - layer - 2, layer - 1, -1):
                tmp_value = current_value
                current_value = matrix[i][matrix_n - layer - 1]
                matrix[i][matrix_n - layer - 1] = tmp_value
            # Go west
            for j in range(matrix_n - layer - 2, layer - 1, -1):
                tmp_value = current_value
                current_value = matrix[layer][j]
                matrix[layer][j] = tmp_value
            
    for i in range(matrix_m):
        line = []
        for j in range(matrix_n):
            line.append(str(matrix[i][j]))
        print " ".join(line)
            

if __name__ == '__main__':
    mnr = raw_input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in xrange(m):
        matrix.append(map(int, raw_input().rstrip().split()))

    matrixRotation(matrix, r)
