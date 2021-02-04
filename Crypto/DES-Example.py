import random,string
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



"""convert string to binary code"""
def con_str_to_bin(input_string):
    exEnc = ""
    for chr in input_string.encode():
        exEnc += format(chr,'08b')+" "
    return exEnc

"""convert binary code to string"""
def con_bin_to_str(input_string):
    exEnc = ""
    for chr in input_string.decode():
        exEnc += format(chr,'08b')+" "
    return exEnc

"""place a space between each character of the string"""
def turn_from_list_to_str(input_str):
    conv_list_to_str = map ( ''.join, zip ( *[ iter ( str ( input_str ) ) ] * 8 ) )
    emp_str = ""
    for ele in conv_list_to_str:
        emp_str += ele+" "
    return emp_str

def bin2text(s): return "".join([chr(int(s[i:i+8],2)) for i in range(0,len(s),8)])

"""Example for DES"""

"""Message"""
message = "This is my secret message"
print("==================message========================================")
print(message)

message = message.split()
for element in message:
    key = randomString ( (len ( element )) )
    key_str_to_bin = con_str_to_bin ( key )
    print ( "==================key========================================" )
    print ( key )
    message_str_to_bin = con_str_to_bin(element)
    print("==================binary representation of message===============")
    print(message_str_to_bin)
    print("==================binary representation of key====================")
    print(key_str_to_bin)
    """convert to int value, base 2"""
    mes_bin = int(message_str_to_bin.replace(" ",""),2)
    key_bin = int(key_str_to_bin.replace(" ",""),2)
    """Carry out XOR which generates one time pad."""
    ciphertext = bin(mes_bin^key_bin)
    ciph_bin = int(ciphertext,2)
    converted_ciphertext = turn_from_list_to_str(ciphertext)
    print("Encrypting Part of Message")
    print("========binary representation XOR between (m^K)===========-")
    print(converted_ciphertext)
    print("Dencrypting Part of Message")
    print("========binary representation XOR between (m^K)^K===========")
    plaintext = bin(ciph_bin^key_bin)
    converted_plaintext = turn_from_list_to_str(plaintext)
    print(converted_plaintext)
    plaintext_to_bin = int(plaintext,2)
    print("========ASCII representation XOR between (m^K)^K===========")
    print(plaintext_to_bin.to_bytes((plaintext_to_bin.bit_length() + 7) // 8, 'big').decode())