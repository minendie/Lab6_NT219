import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
def encrypt (plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    #plaintext = unpad(plaintext, DES.block_size)
    return ciphertext

plaintext = "0000000000000000"
key = "FEFE1F1FFEFE0E0E"
pl_b = bytes.fromhex(plaintext)
key_b = bytes.fromhex(key)
print (pl_b)
print(key_b)
cipher = encrypt(pl_b,key_b)
print(cipher.hex().upper())
