##
## Gaby, 2024
## poc
## File description:
## randomStr
##

# Next step OOBJ to set in object connexion, cursor, context

from dbOps import connectToDb, disconnectFromDb
from tokenGenerator import generateToken
from dataManip import tokenizeData, untokenizeData

import argparse
import time
from dotenv import load_dotenv

def main(args):
    connexion, cursor = connectToDb()
    if args.generate:
        generateToken(args.generate, connexion, cursor)
    elif args.tokenize:
        token = tokenizeData(args.tokenize, connexion, cursor)
        print("token: %s" % token)
    elif args.untokenize:
        data = untokenizeData(args.untokenize, connexion, cursor)
        print("data: %s" % data)
    else:
        print("No argument given, please use -h for help.")
    disconnectFromDb(connexion)

if __name__ == "__main__":
    load_dotenv()
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
    args = parser.parse_args()
    start_time = time.time()
    main(args)
    print("Python execution time: %.6f seconds" % (time.time() - start_time))