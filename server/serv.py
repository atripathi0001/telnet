# Server 
# Server for telnet can be run using servr.sh 

import socket
import sys
import subprocess
import datetime
import log
import login 
import os
import IpAddress

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_ip = IpAddress.getIp()
server_port = sys.argv[1]
server_address = (server_ip, int(server_port))
print >>sys.stderr, 'Starting server up on %s port %s' % server_address 
sock.bind(server_address)
sock.listen(1)

while True:
    print >>sys.stderr, 'Waiting for a connection ..'
    connection, client_address = sock.accept()
    try:
            print >>sys.stderr, 'Client connected : ', client_address

	    UserName = connection.recv(20)#get user name 
	    connection.sendall('a') #send diff
            Passwd = connection.recv(56)#get pass
            if Passwd:
		value, LoginName = login.check(UserName, Passwd)
 
		if (value):
                	connection.sendall(LoginName) # send valid 
			while True:
				command = connection.recv(40) #get command 
		
				if command != "":
					log.write(UserName,command)
				if (command != 'quit'):
					if command.startswith("cd"):
						 try:
						 	os.chdir(command.replace(command[:3], ''))
						 	out = '\n'
						 	err = ''
						 except :
						 	out = "Internal Server Error or File Not Found "
					else:
						try:
							popen = subprocess.Popen(command, 									shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
							out, err = popen.communicate()
						except:
							out = "Internal Server Error"
		
					connection.sendall(out)
				else:
					connection.close()
					break
		else:
			connection.sendall( 'Fail')
			 
            else:
                break
    finally:
        connection.close()
