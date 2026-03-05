import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from dotenv import load_dotenv

load_dotenv()
loadkey = os.getenv("key")
loadiv = os.getenv("iv")

key = bytes.fromhex(loadkey)
iv = bytes.fromhex(loadiv)

def encrypt(text):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
        
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(text.encode()) + padder.finalize()
        
    ct = encryptor.update(padded_data) + encryptor.finalize()

    return ct.hex()
