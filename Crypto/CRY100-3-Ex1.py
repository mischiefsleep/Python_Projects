import base64

Examples = ["Cat","Mouse","Monitor"]

print ("Word\t","Binary\t\t\t\t","Base64")
"""iterate through each string in Examples and convert 
from ASCII => Binary => Base64 then print to console
NOTE Each Base64 digit represents exactly 6 bits of data.
Three 8-bit bytes (i.e., a total of 24 bits) can therefore 
be represented by four 6-bit Base64 digits."""
for ex in Examples:
	exEnc = ""
	for byte in ex.encode():
		exEnc += format(byte,'08b') + " "
	print (ex,"\t",exEnc,"\t",base64.b64encode(ex.encode()))
