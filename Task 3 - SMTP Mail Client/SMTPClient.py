#!/usr/bin/env python
import ssl
from socket import * 
import base64
#from base64 import *  

msg = b"\r\n I love computer networks!"
endmsg = b"\r\n.\r\n"
# Commands reference: https://www.samlogic.net/articles/smtp-commands-reference.htm
# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = ('localhost',587) # local https://www.hmailserver.com mailserver installed.
 
# TODO: Create socket called clientSocket and establish a TCP connection with mailserver  
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024)  
print (recv)
if recv[:3] != b'220':
	print ('220 reply not received from server.' )

# Send HELO command and print server response.  
heloCommand = b'EHLO localhost\r\n'  
clientSocket.send(heloCommand)  
recv1 = clientSocket.recv(1024)
print ("response after ehlo"+recv1.decode())
if recv1[:3] != b'250':
	print('250 reply not received from server.')
 
# TODO: Authentication and enhanced security may be required
#created a self-signed SSL on https://www.selfsignedcertificate.com/ and added it to local mail server
#start secure tls
clientSocket.send(b"STARTTLS \r\n")
recv_tls = clientSocket.recv(1024)
print("Response after starting TLS: "+recv_tls.decode())

#SSL wrap the connection to secure communication
clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)


# Info for username and password for local mail server
username = b"hello@kck.co.zw"
username = base64.b64encode(username)
password = b"hello"
password = base64.b64encode(password)

# Server Authentication with base64 encoded responses
authMsg = b"AUTH LOGIN\r\n"
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print("Auth resp: "+recv_auth.decode())

clientSocket.send(username)
clientSocket.send(b"\r\n")
recv_user = clientSocket.recv(1024)
print("Response after sending username: "+recv_user.decode())

clientSocket.send(password)
clientSocket.send(b"\r\n")
recv_pass = clientSocket.recv(1024)
print("Response after sending password: "+recv_pass.decode())

# TODO: Send MAIL FROM command and print server response.  
mail_from = b"MAIL FROM:<abc@kck.co.zw>\r\n"
clientSocket.send(mail_from)
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: "+recv2)

# TODO: Send RCPT TO command and print server response.  
rcpt_to = b"RCPT TO:<ktrkud001@myuct.ac.za>\r\n"
clientSocket.send(rcpt_to)
recv3 = clientSocket.recv(1024)
print("After RCPT TO command: "+recv3.decode())

# TODO: Send DATA command and print server response.  
data = b"DATA\r\n"
clientSocket.send(data)
recv4 = clientSocket.recv(1024)
print("After DATA command: "+recv4.decode())

# TODO: Send message data.  
clientSocket.send(msg)

# TODO: Message ends with a single period.  
clientSocket.send(endmsg)
recv_msg = clientSocket.recv(1024)
print("Response after sending message body:"+recv_msg.decode())

# TODO: Send QUIT command and get server response.  
quit = b"QUIT\r\n"
clientSocket.send(quit)
recv5 = clientSocket.recv(1024)
print(recv5.decode())
clientSocket.close()
exit(0)