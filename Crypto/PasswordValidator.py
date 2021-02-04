#!/usr/bin/python3
# Python program to check validation of password 
# Module of regular expression is used with search() which will search the input provided for the characters
import re 
# Get user input for password they'd like to use
password = input("What is your password? ")
flag = 0
# While look to first check if the password is long enough, then check for the correct characters in password.
while True:   
    # check length
    if (len(password)<8): 
        flag = -1
        break
    # check for a-z lowercase
    elif not re.search("[a-z]", password): 
        flag = -1
        break
    # check for A-Z uppercase
    elif not re.search("[A-Z]", password): 
        flag = -1
        break
    # check for numbers
    elif not re.search("[0-9]", password): 
        flag = -1
        break
    # final check for special character
    elif not re.search("[_@$#%^&*!]", password): 
        flag = -1
        break
    # check for spaces in password, if there are it's invalid
    elif re.search("\s", password): 
        flag = -1
        break
    # check for the invalid characters we do not want in the passwords
    elif re.search("[.,<>/\~']", password): 
        flag = -1
        break
    # if all the conditions of pw are met, print Valid Password
    else: 
        flag = 0
        print("Valid Password") 
        break
# if conditions aren't met, invalid password.
if flag ==-1: 
    print("Not a Valid Password") 
