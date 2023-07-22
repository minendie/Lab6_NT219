import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
def decrypt (ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    #plaintext = unpad(plaintext, DES.block_size)
    return plaintext


ciphertext_b64 = "6MupHn98v/yhX3jSCMf+LFOVQc7iRLALzTjd5ow34a5vnoPkSmZ1MHG/wU9Elkva"
ciphertext_byte = base64.b64decode(ciphertext_b64)
print(ciphertext_byte)

key_hex = "E001E001F101F101"
key_b = bytes.fromhex(key_hex)
print(key_b)
plaintext = decrypt(ciphertext_byte, key_b)
print("Decrypted plaintext:", plaintext.decode('utf-8'))
