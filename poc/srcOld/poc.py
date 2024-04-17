##
## Gaby, 2024
## poc
## File description:
## randomStr
##

import random
import string
import time
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
        print("Connected to DB (localhost:5432) as gaby")
        return connexion, cursor
    except Exception as e:
        print("Error: ", e)

def addTokenToDB(iteration, cursor, token):
    cursor.execute("insert into my_table values('%s', 'Script Data')" % token)
    print("%i: %s added" % (iteration, token))

def randomStr(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def sha256(string):
    import hashlib
    return hashlib.sha256(string.encode()).hexdigest()

def main(cursor, iteration):
    for i in range(iteration):
        seed = randomStr(16)
        hashed = sha256(seed)
        addTokenToDB(i, cursor, hashed)
        connexion.commit()


if __name__ == "__main__":
    iteration = 10000
    cursor = None
    start_time = time.time()
    connexion, cursor = connectToDB()
    main(cursor, iteration)
    print("Python execution time: %.6f seconds" % (time.time() - start_time))
    connexion.close()

