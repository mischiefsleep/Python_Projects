alpha = input("What is the key?")
cipher = []
print(cipher)
for char in alpha: 
    number = ord(char) - 97
    cipher.append(number)

print(cipher)