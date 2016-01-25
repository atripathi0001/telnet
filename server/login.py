# Function to check for the validity of login credential
# Read the value from file and vlaidate it 
# Input  : UserName and Password
# Output : true or false 

import sys
import path
import log

def check(UserName,Password):
	try:
		filepath = path.GetPath() +  "passfile"

		fp = open(filepath, 'r+')
		for string in fp.readlines():
			username = string.split(":")[0]
			passwrd = string.split(":")[-1]
	 		passwrd = passwrd[:-1]
			name = string.split(":")[1]
			if (Password == passwrd and UserName == username ):
				passwrd = None
				Password = None	
				fp.close()
				log.writeLoginLog(UserName,"Sucessus")
				return 	True, name
		passwrd = None
		Password = None
		fp.close()
		name = 'false'
		log.writeLoginLog(UserName,"Failure")
		return False, name
	except:
		name = 'flase'
		log.writeLoginLog(UserName,"Failure")
		return False, name
