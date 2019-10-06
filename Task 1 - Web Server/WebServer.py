#!/usr/bin/env python

# Import socket module 
from socket import *
import sys # In order to terminate the program 

# TODO: Create a TCP Socket - https://docs.python.org/3/library/socket.html
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# TODO: Assign a host and port number - package in a tuple
host_port = ('localhost', 8080)
# TODO: Bind the socket to the port
server_socket.bind(host_port)
# TODO: Listen to at most 1 connection.
server_socket.listen(1)


# TODO: Establish the connection  
print ('Ready to serve...')

connectionSocket, address = server_socket.accept() #Fill in start #Fill in end  

try: 
    message = connectionSocket.recv(4096)#TODO: Fill in start #Fill in end
    filename = message.split()[1] # ['GET','/file_path.html', 'HTTP/1.1\r\nHost:',...]
    f = open(filename[1:], "r")  #slicing of '/', read mode
    outputdata = f.read()
	# TODO: Send one HTTP header line into socket  
    http_header = b"""\
    HTTP/1.1 200 OK
    
    """ #multiline string to include mandatory blank line.
    connectionSocket.send(http_header)
	#TODO: Send the contents of the requested file to the client  
    connectionSocket.send(str.encode(outputdata))
    connectionSocket.close()  
except IOError:
	# TODO: Send response message for file not found 
    response_404 = b"""\
    HTTP/1.1 200 OK

    <h1>
    404 File not found
    </h1>
    """
    connectionSocket.sendall(response_404)

#TODO: Close client socket  
connectionSocket.close()
