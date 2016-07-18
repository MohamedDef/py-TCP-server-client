import socket

ip=''
port=6000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip,port))
print('Listening to {}'.format(s.getsockname()))
s.listen(1)

while True:
    client,addr=s.accept()
    data=client.recv(1024)
    if data:
        print(data)
        client.send(data)
    client.close()