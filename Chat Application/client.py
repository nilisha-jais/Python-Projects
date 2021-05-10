import socket
chunk=65555
port=3000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
hostname='127.0.0.1'
s.bind((hostname,port))

while True:
    data,clientAdd=s.recvfrom(chunk)
    message=data.decode('ascii')
    print(f"User_2: {message}")
    message_send=input("Type message:")
    data=message_send.encode('ascii')
    s.sendto(data,clientAdd)