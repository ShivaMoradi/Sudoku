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
# convertwra matrixen till NumPy matrix
ngiven = np.matrix(given)
# skriva ut matrixen bara för att se hur ser det ut
print(ngiven)

user_guessed = []  # identifierar en array list med användarens gisade nummret


# gör snyggt matrixen för att bli mer läsbar
def prettify(given):
    print("Output is:  ")
    # börja med kolumn med index 0 och radden med index 0 och titta rad med rad
    j = 0
    for row in given:
        i = 0
        j += 1
        for item in row:
            i += 1
            print(f" {item} ", end='')  # skriva ut vaeje item i matrixen och lägg till en space
            if i % 3 == 0 and i < 9:  # gör sammasak i rad för 3*3 underrutnät och även lägg en | melan varje 3*3 underrutnät
                print(" | ", end='')
        print()  # Skriva ut det
        if j % 3 == 0 and j < 9:  # Till kolumnerna lägg ' - ' 11 gånger för att bli snygast
            print(' - ' * 11)

prettify(given)

# definierar funktion pussel board och idintifierar rad, kolum och siffran som användaren gissar
def board(row, column):
    global ngiven, user_guessed
    number = input("Guesse a number: ")  # En användare kan gissa en siffran mellan 1-9
    try:  # vilkor för att nummret ska vara intiger och mellan 1-9 annars det är fel
        number = int(number)
        if 1 <= number < 10:
            print(f"You guessed: {number}")
        else:
            print(f"The number should be between 1 and 9")
            return False
    except ValueError:
        print(f"Please enter a valid number")
        return False
    # Loopar mellan 0-9 och kontrollerar om nummret är i raden
    for i in range(0, 9):
        if ngiven[row, i] == number:
            print(False)
    # Loopar mellan 0-9 och kontrollera om det finns siffran inne i kolumn?
    for i in range(0, 9):
        if ngiven[i, column] == number:
            print(False)

    # skapar olika sektioner till 3x3-underrutnät
    x0 = (column // 3) * 3  # Sektion börjat från row med index 0 till 2 och * 3 för att skapa nästa sektioner
    y0 = (row // 3) * 3  # Sektion börjat från kolumn med index 0 till 2 och * 3 för att skapa nästa sektioner

    # finns nummret inne i 3x3-underrutnät?
    for i in range(0, 3):
        for j in range(0, 3):
            if ngiven[y0 + i, x0 + j] == number:
                print(False)
    user_guessed.append(
        number)  # lägger gissat nummer inne i användaren gissade listan för att kunna visa listan snyggt
    print(True)


def solve(given):  # Funktion till lösa pussle med backtracking metod
    global user_guessed  # ropar user_guessed för att identifeiea det i Solv funktion och kunna göra det snygt med Pretify funktion
    for row in range(9):  # till alla rader i range 9
        for column in range(9):  # och även till alla kolumner i range 9
            if given[row][column] == 0:  # om cellet är 0
                for number in range(1, 10):  # lägg gissade nummret som är i range 9 i cellet
                    if board(row, column):
                        print(f"user type the number: {number}")  # skriva ut gissade numret bara för att se det
                        given[row][column] = number  # fylla cellet med gissade numret
                        if solve(given):  # om det lösas visa True
                            return True
                        given[row][column] = 0  # gå upp igen i den stegrt som kontrollerar cellet är 0
                return False
    prettify(given)  # skriva ut slut resultat med alla gissade numret som förfinades


solve(given)  # Anropar solve funktionen med givande matrix
