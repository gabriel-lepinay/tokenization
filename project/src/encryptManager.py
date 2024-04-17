from cryptography.fernet import Fernet
import os

def generate_key(path):
    key = Fernet.generate_key()

    with open(path, "wb") as key_file:
        key_file.write(key)
    os.chmod(path, 0o600)

def load_key(path):
    with open(path, "rb") as key_file:
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
