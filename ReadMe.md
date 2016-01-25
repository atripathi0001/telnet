# Telnet Client Server

A simple telnet client server with following features : 

	i)		client autentication 
	ii)		hash password 
	iii)	memory cleaning
	iv)		logs for login and command usage

Future work :

	i)		ecnryption of channel 
	ii)		Server authentication

Note :

1) The pass file contains ```<loginID, UserName, Password>``` tupple seprated by tab in the same order. 

The login credentials are as follows -
```
UserName : User
Password : Password

UserName : Guest
Password : Gpassword
```
2) The command log is saved in the same folder and contains the following tuple  ```<UserName, DateTime, Command> ``` 

Installation:

	1)	Set the path in the path.py pointing to the server folder.
	2)   The default port no is 1010 (can be updated in server.sh and client.sh to chnage)
	3)	Check the port no in clinet.sh and server.sh file and the ip address in client.sh file 
	4)	Run the following command in same order(you might need sudo permission)	
```
server.sh  
client.sh 
```
