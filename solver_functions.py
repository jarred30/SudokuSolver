import numpy as np


def solverMain(puzzle):
    """Main solver function"""
    puzzle, check = formatCheck(puzzle)
    if check:
        return ('Please check the values\n'
                'entered. Only numerical\n'
                'values between 0 and 9\n'
                'are valid. A 0 will be\n'
                'assumed as unknown.')
    if checkPuzzle(puzzle):
        return ('Check sudoku entry.\n'
                'The puzzle entered\n'
                'is not solvable.')
    else:
        solution = solvePuzzle(puzzle)
        return solution


def formatCheck(entry):
    """Checks entry format"""
    puzzle = np.zeros(shape=(9, 9))
    counter = 0
    allowable = list(range(0, 10))
    values = [field.get() for field in entry]
    for i2 in range(0, 9, 1):
        for j2 in range(0, 9, 1):
            if values[counter] == '':
                values[counter] = 0
            if not str(values[counter]).isdigit():
                return puzzle, True
            elif int(values[counter]) not in allowable:
                return puzzle, True
            else:
                puzzle[j2, i2] = values[counter]
            counter = counter + 1
    return puzzle, False


def checkPuzzle(puzzle):
    """Determines if puzzle is possible"""
    for i in range(0, 9, 1):
        for j in range(0, 9, 1):
            temp = puzzle[i, j]
            if temp != 0:
                if checkValue(puzzle, i, j, temp):
                    return True
    return False


def checkValue(puzzle, x, y, value):
    """Returns 1 is value is taken and 0 if not"""
    temp_puzzle = np.copy(puzzle)
    temp_puzzle[x, y] = 0  # ignore own value
    if value in temp_puzzle[x, :] or value in temp_puzzle[:, y]:
        return 1
    else:
        x_base = x // 3 * 3
        y_base = y // 3 * 3
        for i in range(x_base, x_base + 3, 1):
            for j in range(y_base, y_base + 3, 1):
                if value == temp_puzzle[i, j]:
                    return 1
    return 0


def solvePuzzle(puzzle):
    """Solves sudoku puzzle"""
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
                        return test
                    else:
                        solution[i, j] = 0
                    if guess == 9:
                        return [0]
    return solution
