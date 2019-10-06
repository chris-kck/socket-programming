#
# UPD Pinger client.
#
import time
from socket import *
from datetime import datetime

i=1
rcvd=0
clientSocket = socket(AF_INET, SOCK_DGRAM) # Create a UDP DGRAM socket.
clientSocket.settimeout(1) # Timeout of 1 second.
addr = ("127.0.0.1", 12000)# Define server address and port.
print('Pinging localhost [127.0.0.1] with Sequence and time data:')
    
for i in range(11):#Ping 10x
    
    try:
        message = 'Ping Sequence={0} Time={1}'.format(i, datetime.now().time()) # Ping data
        start = time.time() #start timer
        clientSocket.sendto(message.encode(), addr)  # Send ping through socket.
        data, server = clientSocket.recvfrom(1024)
        time.sleep(1) #adding precision to float calculations of time else rtt=0.
        end = time.time()
        rcvd+=1
        rtt = end - start-1 #removing the added second.
        print('Reply from {0}: data={1} server=127.0.0.1 time={2}s'.format(addr[0], data,rtt))

    # If data is not received back from server, print it has timed out.
    except timeout:
        print ('REQUEST TIMED OUT')

print('Ping statistics for {0}: \n Packets sent=10 received={1} {2}% Loss'.format(addr[0], rcvd, ((10-rcvd)*10)))