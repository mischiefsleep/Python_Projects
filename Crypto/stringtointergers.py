#!/usr/bin/python3
# Program to convert a string to list of intergers to use as a key for encryption
lowalph = "abcdefghijklmnopqrstuvwxyz"
numbers = "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,161,7,18,19,20,21,22,23,24,25"

str.replace(lowalph, numbers)

lowalph = lowalph.split(",")

print(lowalph)
