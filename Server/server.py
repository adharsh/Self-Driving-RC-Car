import socket
import serial
import sys
import time

# Assumes in arduino.ino, TIME = 50

TCP_IP = '129.2.200.255' # private ip
TCP_PORT = 5005

a = serial.Serial('\\.\COM1', 115200)

def move(data):
	if data < 7:
		a.write(chr(0).encode())		
	else:
		a.write(chr(1).encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address: ', addr)

while 1:
    data = float(conn.recv(1024).decode())
    move(data)
    print("received data:", data)
    sys.stdout.flush()
conn.close()