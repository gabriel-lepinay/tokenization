from cryptography.fernet import Fernet
import os
import sys

def generate_key():
    key = Fernet.generate_key()

    with open("key", "wb") as key_file:
        key_file.write(key)
    os.chmod("key", 0o600)

def load_key():
    with open("key", "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_data(data, key):
    f_obj = Fernet(key)
    cipher_txt = f_obj.encrypt(data.encode())
    return cipher_txt

def decrypt_data(cipher_txt, key):
    f_obj = Fernet(key)
    plain_txt = f_obj.decrypt(cipher_txt).decode()
    return plain_txt

def main(argc, argv):
    loq = None

    try:
        loq = load_key()
        print('Loaded key:', loq)
    except:
        print('Key not found!')
        print('Generating new key...')
        generate_key()

    if argc == 2:
        cipher_txt = encrypt_data(argv[1], loq)
        print('Encrypted data:', cipher_txt)

    elif argc == 3:
        plain_txt = decrypt_data(argv[2].encode(), loq)
        print('Decrypted data:', plain_txt)


if __name__ == "__main__":
    # get arguments from command line
    main(len(sys.argv), sys.argv)