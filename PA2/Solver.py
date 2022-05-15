import Board
import copy
# Method for Human move with a input check if spot is not valid.
def human_move(matrix, symbol):
    while(True):
        move = input("Please enter row and column (r/c): ")
        row = int(move[0])
        col = int(move[2])
        if(matrix[row-1][col-1] == '-'):
            Board.makeMove(row,col,matrix, symbol)
            break
        else:
            print("Not a Valid Spot")
    return matrix

# Method for AI move with minimax of Depth 1 
def ai_move(matrix, symbol, player):
    row, col, numExpanded = minimax(matrix, player)
    Board.makeMove(row,col,matrix,symbol)
    print("AI move: ", row, "/", col)
    return matrix, numExpanded

# Check for remaining spots in given board 
def check(matrix):
    count = 0
    for row in matrix:
        for col in row:
            if(col == '-'):
                count+=1
    return count

# Minimax function for depth 1 (MULTIPLE DEPTHS NOT FIGURED OUT)
def minimax(matrix, player):
    numExpanded = 0
    tree = []
    rowCount = 0
    temp = copy.deepcopy(matrix)
    #Iterates through the matrix
    for row in temp: 
            rowCount += 1
            colCount = 0
            for col in row:
                colCount+=1
                # If spot is open, create tuple and append to tree
                if(col == '-'):  
                    temp1 = Board.makeMove(rowCount,colCount,temp, "ai")
                    count = check(temp1)
                    tree.append((count, temp1, rowCount, colCount))
                    numExpanded+=1
                    temp = copy.deepcopy(matrix)
    # If AI goes second, find min util value
    if(player == '2'):
        rowF = ((min(tree))[2])
        colF = ((min(tree))[3])
    # If AI goes first, find max util value
    elif(player == '1'):
        rowF = ((max(tree))[2])
        colF = ((max(tree))[3])
    return rowF,colF, numExpanded

def ABminimax(matrix):
    print("was not finished")
    # nodesExpanded = 0
    # tree = []
    # rowCount = 0
    # #Create tree at depth 1
    # temp = copy.deepcopy(matrix)
    # for row in temp: 
    #         rowCount += 1
    #         colCount = 0
    #         for col in row:
    #             colCount+=1
    #             if(col == '-'):  
    #                 temp1 = Board.makeMove(rowCount,colCount,temp, "ai")
    #                 #count = check(temp1)
    #                 tree[temp].append((temp1, rowCount, colCount))
    #                 nodesExpanded+=1
    #                 temp = copy.deepcopy(matrix)

    # rowCount = 0        
    # for node in tree:
    #     temp = copy.deepcopy(node[2])
    #     tempTree = []
    #     #Create tree at depth 2
    #     for row in temp: 
    #         rowCount += 1
    #         colCount = 0
    #         for col in row:
    #             colCount+=1
    #             if(col == '-'):  
    #                 temp1 = Board.makeMove(rowCount,colCount,temp, "ai")
    #                 count = check(temp1)
    #                 tempTree[temp].append(count, temp1, rowCount, colCount)
    #                 temp = copy.deepcopy(node[2])
    #                 nodesExpanded+=1
    # for node in tempTree:
    #     min(tempTree[temp])