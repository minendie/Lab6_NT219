from Crypto.Cipher import AES
import base64
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from pwn import *  

def xor (a,b):
    return bytes(x^y for x,y in zip(a,b))

# ECB: C = ENC(PT2)
# CBC: C = ENC(PT1 ^ iv) doi voi 1 block
#ma enc la ham 1:1 nen PT2 = PT1 ^ iv
# -> PT1 = PT2 ^ iv
plaintxt2 = "KasGehLFmlrEkcu5bJEMnTu3yJln01Bg8unIam8EreWkbZO3GMbV1Vwz5bV2NnAu2LUi8LT0rPQElQq3xSKKh0Mp2Kvx0hE39vfiu9FC9TRl+Dv+kLDeQzg3OK366U0v9OuGG8sbwSPpJILuSjyCYy0+gYueko2Yu8pGa6JNltQ="
cp = "WHRp+kejOKNbmegIBuUXWspNVyb5fUC8fF2Nc8YWBEa5zAKE3BUWSyi1YtgGg+SnNchjINGk0pfWh4p4eDLVTAqKGzoBUWXAGENQTEFYLg+cgmegTHXhUpznI84+TkHPQ1ah5l0xrfB4eSdFok2W1ISmNj45ZC2N96R3VcxzEwg="
iv = "aO5VWmEkIffk9SoCyf9rvQ=="
pt2 = base64.b64decode(plaintxt2)
cpt = base64.b64decode(cp)
iv = base64.b64decode(iv)
ctx = iv + cpt #ctx la gi?
pt1 = xor(pt2,ctx)
print (pt1.decode('utf-8'))
