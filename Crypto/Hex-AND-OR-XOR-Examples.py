# Hexadecimal operations in python with examples
# import the modules required for the script
import base64

Examples = ["Cat","Mouse","Monitor"]


# display first output line
# Word	ASCII	BASE64
print("Word\t"," ASCII\t\t\t\t","Base64")
# Iterate through the elements in Examples List
for ex in Examples:
	exEnc = " "
	for byte in ex.encode():
		exEnc += format(byte,'08b')+" "
	print(ex,exEnc,"\t",base64.b64encode(ex.encode()))

