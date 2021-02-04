#!/usr/bin/python3
# Define the encrypt function that will pad if the key length is not equal to the plain text
# I pulled the function definitions from a code reference at https://everything2.com/title/Permutation+cipher 
# Deleted what was useless for myself and then wrote the rest following the structure I saw there 
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
# I went ahead and assigned the values in a list because I am having trouble with converting STUDENT to numbers.
#alpha = input("What is the key?")
cipher = [4,5,6,7,1,9]
#for char in alpha: 
  #  number = ord(char) - 97
  #  cipher.append(number)
#print(cipher)
# Add text to be encrypted, and convert to upper case
plaintext = input("What is going on").upper()
# Replace the spaces in plain text so they are not added when encrypting
plaintext = plaintext.replace(" ", "")

# encrypt the text and assign it to a variable to use.
ciphertext = encrypt(cipher, plaintext)
ciphertext = ciphertext.replace(" ", "")
# Print the cipher text!
print("Youre encrypted text is: ",ciphertext)