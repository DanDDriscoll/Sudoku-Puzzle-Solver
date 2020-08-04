import numpy as np


def is_safe(puzzle, row, column, value):
    if value not in puzzle[row] and value not in puzzle[:, column]:
        for i in range(3):
            for j in range(3):
                if puzzle[i + (row - row % 3)][j + (column - column % 3)] == value:
                    return False
        return True
    else:
        return False


def solve(puzzle, row=0, col=0):

    for row in range(len(puzzle)):
        for column in range(len(puzzle)):
            if puzzle[row][column] == 0:
                for num in range(1, 10):
                    if is_safe(puzzle, row, column, num):
                        print(puzzle, '\n')
                        puzzle[row][column] = num
                        if solve(puzzle, row, column):
                            return True
                        else:
                            puzzle[row][column] = 0
                return False
    return True


if __name__ == '__main__':
    puzzle = np.array([[7, 0, 2, 0, 0, 4, 0, 0, 6],
                       [0, 3, 0, 9, 0, 8, 0, 0, 7],
                       [0, 0, 4, 0, 0, 0, 9, 0, 1],
                       [0, 0, 0, 0, 0, 0, 7, 0, 4],
                       [0, 0, 6, 0, 0, 0, 3, 0, 0],
                       [0, 0, 1, 0, 9, 2, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 2],
                       [6, 2, 0, 1, 7, 9, 4, 0, 0],
                       [0, 4, 0, 0, 8, 0, 0, 0, 0]])

    if solve(puzzle, 0, 0):
        print(puzzle)
    else:
        print('There is no solution')

