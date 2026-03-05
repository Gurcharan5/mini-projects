import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from dotenv import load_dotenv

load_dotenv()
loadkey = os.getenv("key")
loadiv = os.getenv("iv")

key = bytes.fromhex(loadkey)
iv = bytes.fromhex(loadiv)

def decrypt(hex):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    
    ct_bytes = bytes.fromhex(hex)
    padded_plaintext = decryptor.update(ct_bytes) + decryptor.finalize()
    
    unpadder = padding.PKCS7(128).unpadder()
    pt = unpadder.update(padded_plaintext) + unpadder.finalize()
    return pt.decode()