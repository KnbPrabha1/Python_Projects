import socket

host="localhost"
port=6000


s=socket.socket(socket.AF_INET,socket.SOCKET_STREAM)


s.bind((host,port))

print("Server is listening on : ",port)

s.listen(1)
c,addrs=s.accept()
print("Connection from :",str(addr))

c.send(b"Hello, how are you")
c.send("bye".encode)

msg=c.recv(1024)
 

c.close()