import mysql.connector
db = mysql.connector.connect(

    host="localhost", user="root",
    password="mypassword", database="Sudoku"
)
cursor = db.cursor(dictionary=True)


def save_given_numbers(user, number):
    cursor.execute(f"INSERT INTO Puzzle (id, user, number)"
                   f"VALUES (NULL, '{user}', {number})")
    db.commit()
