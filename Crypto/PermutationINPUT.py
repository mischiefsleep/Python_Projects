def decrypt(cipher, ciphertext):
    return encrypt(inverse_key(cipher), ciphertext)

def encrypt(cipher, plaintext):
    plaintext = "".join(plaintext.split(" ")).upper()
    ciphertext = ""
    for pad in range(0, len(plaintext)%len(cipher)*-1%len(cipher)):
        plaintext += "X"
    for offset in range(0, len(plaintext), len(cipher)):
        for element in [a-1 for a in cipher]:
            ciphertext += plaintext[offset+element]
        ciphertext += " "
    return ciphertext[:-1]

def inverse_key(cipher):
    inverse = []
    for position in range(min(cipher),max(cipher)+1,1):
        inverse.append(cipher.index(position)+1)
    return inverse

cipher = [4,5,7,1,2,3,6]
#print(cipher)
plaintext = "Mary had a little lamb its fleece as white as snow everywhere that mary went the lamb was sure to go".upper()
#print(plaintext)
plaintext = plaintext.replace(" ", "")
#print(plaintext)
ciphertext = encrypt(cipher, plaintext)
print("Youre encrypted text is: ",ciphertext)