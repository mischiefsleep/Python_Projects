#!/usr/bin/python3
# Define the decrypt function that will pad if the key length is not equal to the plain text
# I pulled the function definitions from a code reference at https://everything2.com/title/Permutation+cipher 
# Deleted what was useless for myself and then wrote the rest following the structure I saw there 
def decrypt(cipher, ciphertext):
    return encrypt(inverse_key(cipher), ciphertext)
# Define the encrpyt function I pulled from above source
def encrypt(cipher, plaintext):
    plaintext = "".join(plaintext.split(" ")).upper()
    ciphertext = ""
# Pad with X if the key is longer than plain text by using modulo operators 
    for pad in range(0, len(plaintext)%len(cipher)*-1%len(cipher)):
        plaintext += "X"
    for offset in range(0, len(plaintext), len(cipher)):
        for element in [a-1 for a in cipher]:
            ciphertext += plaintext[offset+element]
        ciphertext += " "
    # Return the padded value to the cipher text
    return ciphertext[:-1]
# This function reverses the key we are using so that we can backwards encrypt, or decrypt the message 
def inverse_key(cipher):
    inverse = []
    for position in range(min(cipher),max(cipher)+1,1):
        inverse.append(cipher.index(position)+1)
    return inverse
# I went ahead and assigned the values in a list because I am having trouble with converting STUDENT to numbers.
cipher = [4,5,7,1,2,3,6]
# add text to be decrypted 
ciphertext = input("What would like to decrypt? ").upper()
# Remove spaces from both texts

ciphertext = ciphertext.replace(" ", "")
# create new plaintext variable based on decrypting the ciphertext
plaintext = decrypt(cipher, ciphertext)
plaintext = plaintext.replace(" ", "")
# Print out the text!!
print("Your decrypted text is: ",plaintext)
