import hashlib
import random
import string
from dbOps import sendTokenToDb

def randomStr(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def sha256(string):
    return hashlib.sha256(string.encode()).hexdigest()

def generateToken(nbTokens, connexion, cursor):
    for i in range(nbTokens):
        seed = randomStr(16)
        hashed = sha256(seed)
        print("%i: generate %s from %s" % (i, hashed, seed))
        try:
            sendTokenToDb(connexion, cursor, hashed)
        except Exception as e:
            raise Exception from e
    
