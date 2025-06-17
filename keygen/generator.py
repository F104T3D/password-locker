from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("keygen/key.key", "wb") as key_file:
        key_file.write(key)