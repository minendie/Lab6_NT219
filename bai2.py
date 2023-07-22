import math

e = 6131
n = 10050256277
ciphertext = 283818407

# Tính private key d
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

_, _, d = extended_gcd(e, n)

# Giải mã ciphertext
plaintext = pow(ciphertext, d, n)
print(plaintext)
plaintext_ascii = bytearray.fromhex(hex(plaintext)[2:]).decode()

print(plaintext_ascii)

