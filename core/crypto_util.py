from cryptography.fernet import Fernet
import os

KEY_PATH = "assets/secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_PATH):
        generate_key()
    with open(KEY_PATH, "rb") as f:
        return f.read()

class Encryptor:
    def __init__(self):
        self.key = load_key()
        self.fernet = Fernet(self.key)

    def encrypt(self, message: str) -> str:
        return self.fernet.encrypt(message.encode()).decode()

    def decrypt(self, encrypted_message: str) -> str:
        return self.fernet.decrypt(encrypted_message.encode()).decode()
