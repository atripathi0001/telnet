# Function to log the details of user command and login attempts 
# The tupple save is <UserName	DateTime  Command> / <UserName	DateTime  loginStatus>
# Input  : UserName and Command/Status
# Output : NA(make the entry to log file in format specified above) 

import datetime
import path

def write(UserName,Command):
	try:
		filepath = path.GetPath() +  "log"
		log = UserName +'\t'+ str(datetime.datetime.utcnow()) +'\t'+  Command
		flog = open(filepath, 'a+')
		flog.write(str(log))
		flog.write("\n")
	except:	
		flog.close()

def writeLoginLog(UserName,Status):
	try:
		filepath = path.GetPath() +  "loginlog"
		log = UserName +'\t'+ str(datetime.datetime.utcnow()) +'\t'+  Status
		flog = open(filepath, 'a+')
		flog.write(str(log))
		flog.write("\n")
	except:	
		flog.close()
