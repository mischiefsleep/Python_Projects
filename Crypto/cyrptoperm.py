def permutationCipher(password, key):
    table =  str.maketrans(string.ascii_lowercase, key)
    return str(password).translate(table)