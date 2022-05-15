from functools import total_ordering
import Board
import Solver
import sys

userInput = sys.argv
# Player is who goes first
player = userInput[1]
# MM or AB
type = userInput[2]

# Create Empty Board
matrix = Board.create_Board()

# Start function
def start(matrix):
    totalNumExpanded = 0
    if(type == 'MM'):
        # Human Goes First
        if(player == '2'):
            while(True):
                # Print start board of current turn
                Board.print_Board(matrix)
                # Takes in Human Move
                matrix = Solver.human_move(matrix, 'O')
                # Checks if win
                if(Solver.check(matrix) == 0):
                    Board.print_Board(matrix)
                    print("human wins")
                    break
                # Else proceed to Player 2
                else:
                    matrix, numExpanded = Solver.ai_move(matrix, 'X', player)
                    totalNumExpanded += numExpanded
                # Check if Win
                if(Solver.check(matrix) == 0):
                        Board.print_Board(matrix)
                        print("ai wins")
                        break
        # Human Goes Second
        elif(player == '1'):
            while(True):
                Board.print_Board(matrix)
                matrix, numExpanded = Solver.ai_move(matrix, 'O', player)
                totalNumExpanded += numExpanded
                Board.print_Board(matrix)
                if(Solver.check(matrix) == 0):
                    Board.print_Board(matrix)
                    print("ai wins")
                    break
                else:
                    matrix = Solver.human_move(matrix, 'X')
                if(Solver.check(matrix) == 0):
                    Board.print_Board(matrix)
                    print("human wins")
                    break
    ### AB WAS NOT FINISHED 
    elif(type == 'AB'):
        Solver.ABminimax(matrix)
    # README FILE THAT PRINTS TOTAL NUMBER OF NODES EXPANDED
    file = open("README.txt", "w")
    file.write("Utility Value Function: Number of remaining available positions" + "\n")
    file.write("Total Number of Nodes Expanded: " + str(totalNumExpanded) + "\n")
    file.write("Depth Level: 1")
    file.close()
# Start
start(matrix)

