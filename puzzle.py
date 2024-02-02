# importerar NumPy
import numpy as np

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
print(ngiven)


def board(row, column, number):  # definiera funktion till pussel
    global ngiven
    # finns siffran inne i raden?
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

board(1,0, 7)
