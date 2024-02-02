# importerar NumPy
import numpy as np
from pandas.core.interchange import column

# Skapa en np grid/matrix med given siffror
given = [
    [1, 0, 4, 0, 0, 6, 7, 0, 0],
    [0, 2, 8, 0, 0, 3, 9, 0, 0],
    [6, 0, 0, 0, 1, 7, 2, 0, 0],
    [2, 5, 0, 0, 0, 9, 0, 3, 4],
    [3, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 4, 1, 0, 3, 0, 6, 0, 0],
    [0, 7, 2, 0, 4, 0, 0, 8, 9],
    [0, 0, 0, 0, 8, 0, 0, 0, 5],
    [9, 3, 0, 0, 0, 0, 0, 2, 1]
]
ngiven = np.matrix(given)


# skriva ut matrixen

def board(row, column, number):  # definiera funktion till pussel
    global ngiven
    print(f"Guesse a number: ")  # En användare kan gissa en siffran mellan 1-9
    try:
        number = int(number)
        if 1 <= number < 10:
            print(f"You guessed: {number}")
        else:
            print(f"The number should be between 1 and 9")
            return False
            # finns siffran inne i raden?
    except ValueError:
        print("Please")
        return False

    for i in range(0, 9):
        if ngiven[row, i] == number:
            print(False)
        # finns siffran inne i column?
    for i in range(0, 9):
        if ngiven[i, column] == number:
            print(False)
        # finns siffran inne i 3x3-underrutnät
        # skapar olika sektioner till 3x3-underrutnät
    x0 = (column // 3) * 3  # Sektion börjat från row med index 0 till 2 och * 3 for skapa nästa sektioner
    y0 = (row // 3) * 3  # Sektion börjat från column med index 0 till 2 och * 3 for skapa nästa sektioner
    for i in range(0, 3):
        for j in range(0, 3):
            if ngiven[y0 + i, x0 + j] == number:
                print(False)
    print(True)


def prettify():
    print("Output:  ")
    global given
    j = 0
    for row in given:
        i = 0
        j += 1
        for item in row:
            i += 1
            print(f" {item} ", end='')
            if i % 3 == 0 and i < 9:
                print(" | ", end='')
        print()
        if j % 3 == 0 and j < 9:
            print(' - ' * 11)


def solve():
    global ngiven
    for row in range(9):
        for column in range(9):
            if given[row][column] == 0:
                for number in range(1, 10):
                    if board(row, column, number):
                        given[row][column] = number
                        if solve():
                            return True
                        given[row][column] = 0
                return False
    prettify()


prettify()
solve()
