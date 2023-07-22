import base64
from Crypto.Cipher import AES

iv = "yIwZn0RUXvlw9lxtVhCuOg=="
cipher = "XEkdm4AGP6oQK0OfKhN7a/fTBb+XyUMlKOHAKoPW7wUzrcbuJnj40jaCfVVilHmLU1V/dXIltUF8dsAhC8LDBIIBhvKzDucvYRwg1HwX9zAwxmeRIq9qFs6+ei80sAzensdBiyF36TpxPefsJRJTRJfqaO7FV6LLT20GkZrqolaKEXEzuWAB+SuWqaoB+ruVH9VPmCH6I8PvfdDA+0bEt1XC4otSHMSDc9X5fDoUs796oPpHuJeANALNr1s9V2E+VFreZkn225Zcldc+XeueBjyg4uy0SwJlteoYvF/tV3U="
plaintext2 = "hU+6vyyX7ZhQtxk+dtQ//OyopjjjJkvC8ZDy/Ap7EopMVGuf46GAkUaG4Fv2t88wE86uD53Rm/JYRv47BbQa45D4ER1SSXbhXDekRVmttmrmSuOLny60WgNeWaAZZNsQY64O91b9BWG9klpiXchPsfKyLOVSV5/50R2siVxXKzT2hBuHqjmM6wGphfy6icq3MbgSE9ekgpdMtsdpoYObUY4T/3maWUDjnJxqb4tmvFbvfZKrlo0lOPD1jRTbrwLcWsiTpgMQ7hRgrI85++eAhc85/gWPV/v0vS90UHPonQU="


iv = base64.b64decode(iv)

cipher = base64.b64decode(cipher)

plaintext2 = base64.b64decode(plaintext2)
print(len(iv))
print(len(cipher))
print(len(plaintext2))

list_cipher_block = []
list_plaintext2_block = []
list_plaintext_block = []
for i in range(0, len(cipher), 16):
    list_cipher_block.append(cipher[i:i+16])

for i in range(0, len(plaintext2), 16):
    list_plaintext2_block.append(plaintext2[i:i+16])

#bytes([a ^ b for a, b in zip(bytes1, bytes2)])
for i in range(len(list_cipher_block)):
    if i == 0 :
        tmp = bytes([a ^ b for a , b in zip(list_plaintext2_block[0],iv) ])
        list_plaintext_block.append(tmp)
    else:
        tmp = bytes([a ^ b for a , b in zip(list_plaintext2_block[i],list_cipher_block[i-1]) ])
        list_plaintext_block.append(tmp)

flag = bytes().join(list_plaintext_block)


print(flag.decode())



    

