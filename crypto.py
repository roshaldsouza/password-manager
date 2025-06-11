from cryptography.fernet import Fernet
import base64

class Crypto:
    def __init__(self, master_key: str):
        if not master_key:
            raise ValueError("Master key cannot be empty!")
        key = base64.urlsafe_b64encode(master_key.ljust(32)[:32].encode())
        self.cipher = Fernet(key)

    def encrypt(self, plaintext: str) -> str:
        return self.cipher.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext: str) -> str:
        return self.cipher.decrypt(ciphertext.encode()).decode()