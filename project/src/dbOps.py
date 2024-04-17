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
        return connexion, cursor
    except Exception as e:
        raise Exception(e) from e

def disconnectFromDb(connexion):
    try:
        connexion.close()
    except Exception as e:
        print("[Disconnect] Database disconnection error:", e)

def sendTokenToDb(connexion, cursor, data):
    try:
        cursor.execute("INSERT INTO my_table (id, token, id_app, raw_data) VALUES ('ID', '%s', 'ID_APP','EMPTY')" % data)
        connexion.commit()
    except Exception as e:
        print("[Send token] SQL error:", e)
        raise Exception from e

def getNoAssociatedToken(cursor):
    try:
        cursor.execute("SELECT * FROM my_table WHERE raw_data = 'EMPTY' LIMIT 1;")
        result = cursor.fetchone()
        return result
    except Exception as e:
        print("[Get empty token] SQL error:", e)

def tokenizeDataToDb(connexion, cursor, token, data):
    try:
        cursor.execute("UPDATE my_table SET raw_data = '%s' WHERE token = '%s';" % (data, token))
    except Exception as e:
        print("[Tokenize data] SQL error:", e)
        raise Exception from e

def untokenizeDataToDb(connexion, cursor, token):
    try:
        cursor.execute("SELECT * FROM my_table WHERE token = '%s';" % token)
        result = cursor.fetchone()
        return result[3]
    except Exception as e:
        print("[Untokenize data] SQL error:", e)
        raise Exception from e

