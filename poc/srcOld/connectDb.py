##
## Gaby, 2024
## poc
## File description:
## connectDb
##

import psycopg2

def connectToDB():
    try:
        connexion = psycopg2.connect(
            host="localhost",
            port="5432",
            database="tokenDb",
            user="gaby",
            password="2727"
        )
        connexion.autocommit = True
        cursor = connexion.cursor()
        print("Connected to DB")
        return connexion, cursor
    except Exception as e:
        print("Error: ", e)

def addTokenToDB(cursor, token):
    cursor.execute("insert into my_table values('2627SFSZ837G', 'Script Data')")
    print("Token added to DB")

if __name__ == "__main__":
    cursor = None
    connexion, cursor = connectToDB()
    addTokenToDB(cursor, "123639862896296239")
    connexion.commit()
    connexion.close()
