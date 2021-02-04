#!/usr/bin/python3
# Define the encrypt function that will pad if the key length is not equal to the plain text
# I pulled the function definitions from a code reference at https://everything2.com/title/Permutation+cipher 
# Deleted what was useless for myself and then wrote the rest following the structure I saw there 
# Define the decrypt function we are going to use
def decrypt(cipher, ciphertext):
    return encrypt(inverse_key(cipher), ciphertext)
    
def encrypt(cipher, plaintext):
    plaintext = "".join(plaintext.split(" ")).upper()
    ciphertext = ""
# Function to invert the key so we can un do the encryption
def inverse_key(cipher):
    inverse = []
    for position in range(min(cipher),max(cipher)+1,1):
        inverse.append(cipher.index(position)+1)
    return inverse
    # Pad with X if the key is longer than plain text by using modulo operators 
    for pad in range(0, len(plaintext)%len(cipher)*-1%len(cipher)):
        plaintext += "X"
    for offset in range(0, len(plaintext), len(cipher)):
        for element in [a-1 for a in cipher]:
            ciphertext += plaintext[offset+element]
        ciphertext += " "
    # Return the padded value to the cipher text
    return ciphertext[:-1]
# I went ahead and assigned the values in a list because I am having trouble with converting STUDENT to numbers.
cipher = [4,5,7,1,2,3,6]
#print(cipher)
ciphertext = "YHDMARA TTEALIL BISLAMT ECAFLEE ITASWHE OWVSSNE WHRERYE ATAETHM ENTRYWT AMWHELB URTASSE XXXOGOX".upper()
#print(plaintext)
#ciphertext = ciphertext.replace(" ", "")
#print(plaintext)
plaintext = decrypt(cipher, ciphertext)
print("Your decrypted text is: ",plaintext)

#ciphertext = "OELMR PUIMS OODRL IASMT TOENC ETSEC URTAE IIDSP IGCEN IXLXT"
#plaintext = decrypt(cipher, ciphertext)