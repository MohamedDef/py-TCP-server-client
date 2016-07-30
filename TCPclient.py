#!/usr/bin/python3
import socket

ip='localhost'
port=6000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
send_data='Hello.'
s.send(send_data.encode('utf-8'))
recv_data=s.recv(1024)
s.close
print('Recieved: ',recv_data.decode('utf-8'))
