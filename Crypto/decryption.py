#!/usr/bin/python3
# ohlittlebrain@gmail.com
# 8/14/2019
# my ceasar cipher
# reference for code : Ahttps://stackoverflow.com/questions/20269330/how-to-make-a-caesar-cipher-work-with-input-that-has-spaces-in-python
# gets user input on what to encrypt and the rotation of cipher.
sentence = input("Please insert a sentence to decrypt: ")
rotation = input("Pick a rotation for the cipher: ")
#
# set rotation to interger and sentence to list.
rotation = int(rotation)
letters = list(sentence)
cipher = ''
# create list for alphabet characters.
ceasar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','m','n','o','o','p','q','r','s','t','u','v','w','x','y','z']
# set limit for cipher
limit = 25
# statment to swap letters based on rotation chose from input
for letter in letters:
    if letter in ceasar:
        oldindex = ceasar(letter)
        newindex = ((oldindex - rotation) % 26)
        newletter = ceasar[newindex]
    else:
        newletter = letter

    print(newletter, end="")
    