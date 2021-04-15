import socket
import sys	

try:
	ip = sys.argv[1]
except:
	print "  USAGE: python port-scanner.py <IPv4_Address>"
	print "EXAMPLE: python port-scanner.py 192.168.1.1"
	exit()
	

for port in range(1, 200):
	try:

		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	
		conn.settimeout(.25) 		

		conn.connect((ip, port))
	

	
		print "Port %i is open." % port		
		conn.close()

	except socket.timeout:
		print "Port %i is filtered." % port


 
	except socket.error:
		print "Port %i is closed." % port		
