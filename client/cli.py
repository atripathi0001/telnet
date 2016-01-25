# Client 
# Client for telnet can be run using servr.sh 


import socket
import sys
import hashlib
import getpass
import os

#Get Host Name and Port Number from user 
server_ip = sys.argv[1]
server_port = sys.argv[2]

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = socket.create_connection((server_ip, int(server_port)))
print >>sys.stderr
 
try:
    
    # Send data
    usrName = raw_input("Username : ")
    passwrd = hashlib.sha224(getpass.getpass()).hexdigest()
    sock.sendall(usrName)# send user name 
    date1 = sock.recv(1) # diff between two 
    sock.sendall(passwrd)# send pass
    passwrd = None 
    usrName = None 
    data = sock.recv(20) # get pass fail 
     
    if data != 'Fail':
	print "Welcome !!"
	print "Enter \"quit\" to terminate the program."
	while True:
		  
		  cmd = raw_input("%s # " % data)
		  sock.sendall(cmd) # send commad 
		  if  cmd == '':
			continue
		  if cmd == 'quit': 
			exit()
		  output = sock.recv(10000) #getoutput
		  print output
    else:
	print 'Login Fail.'
finally:
    print >>sys.stderr, 'Bye !!'
    sock.close()
