from cryptography.fernet import Fernet

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()

if __name__ == "__main__":
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
