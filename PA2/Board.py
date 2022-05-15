import math
import Solver
bSize = 6
# Creates empty board of size 7
def create_Board():
    matrix = []
    for x in range(bSize):
        temp = []
        for j in range(bSize):
            temp.append('-')
        matrix.append(temp)
    return matrix

def makeMove(row,col, matrix, symbol):
    row = row-1
    col = col-1

    matrix[row][col] = symbol
    
    if(row > 0 and col > 0 and row < bSize - 1 and col < bSize - 1):
        matrix[row-1][col-1] = '/'
        matrix[row-1][col] = '/'
        matrix[row-1][col+1] = '/'
        matrix[row][col+1] = '/'
        matrix[row][col-1] = '/'
        matrix[row+1][col-1] = '/'
        matrix[row+1][col] = '/'
        matrix[row+1][col+1] = '/'
    elif(row == 0 and col > 0 and col < bSize - 1):
        matrix[row][col+1] = '/'
        matrix[row][col-1] = '/'
        matrix[row+1][col-1] = '/'
        matrix[row+1][col] = '/'
        matrix[row+1][col+1] = '/'
    elif(row > 0 and col == 0 and row < bSize - 1):
        matrix[row-1][col] = '/'
        matrix[row-1][col+1] = '/'
        matrix[row][col+1] = '/'
        matrix[row+1][col] = '/'
        matrix[row+1][col+1] = '/'
    elif(row == 0 and col == 0):
        matrix[row][col+1] = '/'
        matrix[row+1][col] = '/'
        matrix[row+1][col+1] = '/'
    elif(row == bSize - 1 and col < bSize - 1):
        matrix[row-1][col-1] = '/'
        matrix[row-1][col] = '/'
        matrix[row-1][col+1] = '/'
        matrix[row][col+1] = '/'
        matrix[row][col-1] = '/'
    elif(row < bSize - 1 and col == bSize-1):
        matrix[row-1][col-1] = '/'
        matrix[row-1][col] = '/'
        matrix[row][col-1] = '/'
        matrix[row+1][col-1] = '/'
        matrix[row+1][col] = '/'
    elif(row == bSize - 1 and col == bSize -1):
        matrix[row-1][col-1] = '/'
        matrix[row-1][col] = '/'
        matrix[row][col-1] = '/'
    return matrix

def print_Board(matrix):
    for x in matrix:
        print(x)

def util (matrix):
    count = Solver.check(matrix)
    return count



