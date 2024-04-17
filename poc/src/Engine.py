from dbOps import connectToDb, disconnectFromDb
from tokenGenerator import generateToken
from dataManip import tokenizeData, untokenizeData
import argparse

class Engine:
    def __init__(self):
        self.args = None
        self.connexion = None
        self.cursor = None
        self.init_args()
        self.init_connexion()

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
            help='associate a token from <str> and store it in the database'
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
        self.args = parser.parse_args()

    def init_connexion(self):
        self.connexion, self.cursor = connectToDb()

    def run(self):
        if self.args.generate:
            generateToken(self.args.generate, self.connexion, self.cursor)
        elif self.args.tokenize:
            token = tokenizeData(self.args.tokenize, self.connexion, self.cursor)
            print("token: %s" % token)
        elif self.args.untokenize:
            data = untokenizeData(self.args.untokenize, self.connexion, self.cursor)
            print("data: %s" % data)
        else:
            print("No argument given, please use -h for help.")

    def destroy(self):
        disconnectFromDb(self.connexion)



