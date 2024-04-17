from dbOps import connectToDb, disconnectFromDb
from tokenGenerator import generateToken
from encryptManager import encrypt_data, decrypt_data, generate_key, load_key
from dbOps import getNoAssociatedToken, tokenizeDataToDb, untokenizeDataToDb
import argparse

class Engine:
    def __init__(self, mode="cli"):
        self.args = None
        self.connexion = None
        self.cursor = None
        self.key = None
        self.path = None
        self.mode = mode

        try:
            if self.mode == "cli":
                self.init_args()
                self.init_encryption()
                self.init_connexion()
            elif self.mode == "api":
                self.path = './.keyVault'
                try:
                    self.key = load_key(self.path)
                except:
                    print("No encryption key found at %s" % self.path)
                self.init_connexion()
        except Exception as e:
            print("Initialization error:\n", e)
            exit(1)

    def printv(self, message, *args):
        if self.mode == "cli" and self.args.verbose:
            print(message, *args)

    def init_encryption(self):
        if self.args.path != None:
            self.path = self.args.path
        else:
            self.path = './.keyVault'
        try:
            self.key = load_key(self.path)
        except:
            if self.args.force:
                generate_key(self.path)
                self.printv("New key file created")
                self.key = load_key(self.path)
            else:
                print("No key file found, please use -f to force the creation of a new key file or specify the path with -p")
                exit(1)

    def init_args(self):
        parser = argparse.ArgumentParser(
            prog='Poc',
            description='Poc of the tokenization project',
            epilog='Created in 2024 by Gabriel Lepinay'
        )
        parser.add_argument(
            '-g', '--generate',
            type=int,
            help='generate <int> tokens and store them in the database'
        )
        parser.add_argument(
            '-t', '--tokenize',
            type=str,
            help='associate a token from <str> and store it in the database. /!\ Str lenght must be < 128'
        )
        parser.add_argument(
            '-ut', '--untokenize',
            type=str,
            help='get the original data from <str> token'
        )
        parser.add_argument(
            '-v', '--verbose',
            action='store_true',
            help='print the result of the operations'
        )
        parser.add_argument(
            '-f', '--force',
            action='store_true',
            help='force actions like generation of a new token when needed, or creation of a new key file if not found'
        )
        parser.add_argument(
            '-p', '--path',
            type=str,
            help='specify the <str> path of the encryption key file (default: ./.keyVault)'
        )
        self.args = parser.parse_args()

    def init_connexion(self):
        self.connexion, self.cursor = connectToDb()
        self.printv("Connected to DB")

    def generateToken(self, number):
        try:
            generateToken(number, self.connexion, self.cursor)
        except Exception as e:
            print("Token generation error:\n", e)
            return None
        return number

    def tokenizeData(self, data):
        row = getNoAssociatedToken(self.cursor)
        if row == None:
            if self.args.force:
                generateToken(1, self.connexion, self.cursor)
                return self.tokenizeData(data)
            else:
                print("No available token found, use -f to force generate a token or -g <int> to generate a specific number of token")
                return None
        self.printv("Token found:", row[1])
        cipher_data = encrypt_data(data, self.key)
        cipher_data = str(cipher_data)
        cipher_data = cipher_data.split("'")[1]
        self.printv("Len cipher:", len(cipher_data))
        try:
            tokenizeDataToDb(self.connexion, self.cursor, row[1], cipher_data)
        except Exception as e:
            return None
        return row[1]

    def untokenizeData(self, token):
        try:
            cipher_data = untokenizeDataToDb(self.connexion, self.cursor, token)
            data = decrypt_data(cipher_data, self.key)
        except Exception as e:
            return None
        return data

    def run(self):
        if self.args.generate:
            self.generateToken(self.args.generate)
        elif self.args.tokenize:
            token = self.tokenizeData(self.args.tokenize)
            if token != None:
                self.printv("Result:\n\tData: %s\n\tAssociated token: %s" % (self.args.tokenize, token))
        elif self.args.untokenize:
            data = self.untokenizeData(self.args.untokenize)
            if data != None:
                self.printv("Result:\n\tToken: %s\n\tRaw data: %s" % (self.args.untokenize, data))
        else:
            print("No argument given, use -h for help.")

    def destroy(self):
        disconnectFromDb(self.connexion)
        self.printv("Disconnected from DB")



