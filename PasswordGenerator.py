import hashlib
usrString = raw_input("Enter string to hash : ")
PasswordHash = hashlib.sha224(usrString).hexdigest()
print PasswordHash
