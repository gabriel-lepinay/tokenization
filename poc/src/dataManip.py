from dbOps import getNoAssociatedToken, tokenizeDataToDb, untokenizeDataToDb

def tokenizeData(data, connexion, cursor):
    row = getNoAssociatedToken(cursor)
    tokenizeDataToDb(connexion, cursor, row[0], data)
    return row[0]

def untokenizeData(token, connexion, cursor):
    data = untokenizeDataToDb(connexion, cursor, token)
    return data
