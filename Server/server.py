import socket
import serial

a = serial.Serial('\\.\COM1', 115200)
a.write(chr(1))

# TCP_IP = '129.2.200.255' //private ip
# TCP_PORT = 5005
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((TCP_IP, TCP_PORT))
# s.listen(1)
#
# conn, addr = s.accept()
# print('Connection address: ', addr)
# while 1:
#     data = float(conn.recv(1024).decode())
#     print("received data: ", data)
# conn.close()