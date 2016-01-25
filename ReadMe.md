# Telnet Client Server

A simple telnet client server with following features : 
	i)client autentication 
	ii)hash password 
	-memory cleaning
	-login attempt log

Future work 
	-ecnryption of channel 
	-Server authentication


The pass file contains loginID, UserName and Password tupple seprated by colon in the same order. The login credentials are as follows -

UserName : User
Password : Password

UserName : Guest
Password : Gpassword

The log is saved in the same folder and contains the following tuple:<UserName	DateTime  Command> 

Installation:

Set the path in the path.py file to the server folder. follow the instructions in the file.
check the port no in clinet.sh and server.sh file and the ip address in client.sh file 
Run server.sh  and then client.sh 

