#!/usr/bin/python3
import string
# Get plain text or user input
plaintext = "Mary had a little lamb its fleece as white as snow everywhere that mary went the lamb was sure to go".upper()
print("plaintext : ",plaintext)
# Get key
key = "student".upper()
print("key : ",key)
# get length of key
keyLength = len(key)
# Get rid of spaces
plaintext = plaintext.replace(" ", "")
print("plaintext : ",plaintext)
# Get rid of punctuation
#plaintext = plaintext.translate(string.punctuation)
print(plaintext)
# Get length of plain text
ptLength = len(plaintext)
# Get the remainder of the PT length / key length
remainder = (ptLength % keyLength)
print(remainder)
# while PT % KL != 0 then + x (add one to ptlength)
while remainder != 0:
    remainder += 1
    
# separate pt into key length segments

# get indicies of key characters if alphabetized(make letters numbers)

# use indicies to re order plain text characters line by line
# repeat this with loop til no lines left

# Print encyrpted script to a file