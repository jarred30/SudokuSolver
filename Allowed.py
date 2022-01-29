# determines allowed values for the space
import numpy as np

# function returns 1 if value is taken and 0 if not
def checkValue(puzzle, x, y, value):
    taken = 0
    if value in puzzle[x, :]:
        taken = 1
    elif value in puzzle[:, y]:
        taken = 1
    else:
        xbase = x//3*3
        ybase = y//3*3
        for i in range(xbase, xbase+3, 1):
            for j in range(ybase,ybase+3, 1):
                if value == puzzle[i, j]:
                    taken = 1
    return(taken)

def solvePuzzle(puzzle):
    solution = puzzle
    test = [0]
    for i in range(0, 9, 1):
        for j in range(0, 9, 1):
            if solution[i, j] == 0:
                for guess in range(1, 10, 1):
                    if checkValue(solution, i, j, guess) == 0:
                        solution[i, j] = guess
                        test = solvePuzzle(solution)
                    if 0 not in test:
                        return(test)
                    else:
                        solution[i, j] = 0
                    if guess == 9:
                        return([0])
    return(solution)

# backtracking
puzzle = np.matrix([[5, 3, 3, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]])

solution = solvePuzzle(puzzle)
if 0 in solution:
    print('no solution')
else:
    print(solution)