import psycopg2
import os

def connectToDb():
    try:
        connexion = psycopg2.connect(
            host=os.getenv('DBHOST'),
            port=os.getenv('DBPORT'),
            database=os.getenv('DBNAME'),
            user=os.getenv('DBUSER'),
            password=os.getenv('DBPASS')
        )
        connexion.autocommit = True
        cursor = connexion.cursor()
        print("Connected to DB")
        return connexion, cursor
    except Exception as e:
        print("Error while trying to connect to database: ", e)

def disconnectFromDb(connexion):
    try:
        connexion.close()
        print("Disconnected from DB")
    except Exception as e:
        print("Error while trying to disconnect from database: ", e)

def sendTokenToDb(connexion, cursor, data):
    try:
        cursor.execute("INSERT INTO my_table VALUES('%s', 'Generated data')" % data)
        print("%s added to database" % data)
        connexion.commit()
    except Exception as e:
        print("Error while trying to send token to database: ", e)

def getNoAssociatedToken(cursor):
    try:
        cursor.execute("SELECT * FROM my_table WHERE raw_data = 'Generated data' LIMIT 1;")
        result = cursor.fetchone()
        if result:
            print("NoAssociated token found")
        else:
            print("No available token found, need to generate more")
        return result
    except Exception as e:
        print("Error while trying to get a no associated token: ", e)

def tokenizeDataToDb(connexion, cursor, token, data):
    try:
        cursor.execute("UPDATE my_table SET raw_data = '%s' WHERE token = '%s';" % (data, token))
    except Exception as e:
        print("Error while trying to tokenize data: ", e)

def untokenizeDataToDb(connexion, cursor, token):
    try:
        cursor.execute("SELECT * FROM my_table WHERE token = '%s';" % token)
        result = cursor.fetchone()
        return result[1]
    except Exception as e:
        print("Error while trying to untokenize data: ", e)

