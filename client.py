import socket
host ='127.0.0.1'
port =  123
with socket.socket(socket.AF_INET, socket.SOCK_STREAM)  as s:
    s.connect((host, port))
    s.sendall(b'hello, world weclome to networking in python')
    data =s.recv(80)
print("Received", repr(data))
