# Second Example for PATH CRY 100 DAY 2
#!/usr/bin/python3
import hashlib

mystring="This is string"

print(hashlib.md5(mystring.encode()).hexdigest())

print(hashlib.sha1(mystring.encode()).hexdigest())

print(hashlib.sha256(mystring.encode()).hexdigest())
