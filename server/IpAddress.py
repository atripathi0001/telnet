# Function to retrieve the ip address of the system
# It returns the IP address of the server so no need to configure it.
# Input  : NA
# Output : IPv4 Address of the machine on which server is hosted.
import socket

def getIp():
	try:
	    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	    s.connect(('<broadcast>', 0))
	    return s.getsockname()[0]
	except:
	    return False	
	
