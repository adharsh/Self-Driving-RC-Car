import socket
import time

TCP_IP = '129.2.200.255' //server ip
TCP_PORT = 5005
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

i = 0
while 1:
    i += 1
    s.send(str(i).encode())
    time.sleep(0.5)
    
s.close() 
print('received data: ', data)