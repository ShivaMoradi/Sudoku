# importerar NumPy
import numpy
import numpy as np
# Skapa en np grid/matrix med given siffror
given = [[1,0,4,0,0,6,7,0,0],
         [0,2,8,0,0,3,9,0,0],
         [6,0,0,0,1,7,2,0,0],
         [2,5,0,0,0,9,0,3,4],
         [3,0,0,0,7,0,0,0,0],
         [0,4,1,0,3,0,6,0,0],
         [0,7,2,0,4,0,0,8,9],
         [0,0,0,0,8,0,0,0,5],
         [9,3,0,0,0,0,0,2,1]]

ngiven = np.matrix(given)
# skriva ut type av np matrix och själva matrixen
print(type(ngiven))
print(ngiven)
number = input(f"Guesse a number: ")
def puzzle(row, column, number): # definiera funktion till pussel
    global ngiven
    # finns siffran inne i raden?
    for i in range(0, 9):
        if ngiven[row][i] == number:
            return False
    # finns siffran inne i column?
    for j in range(0, 9):
        if ngiven[column][j] == number:
            return False
# finns siffran inne i 3x3-underrutnät .


