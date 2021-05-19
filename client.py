import socket

s = socket.socket()
port = 3125
s.connect(('localhost', port))
z = 'Welcome Skanda '
s.sendall(z.encode())    
s.close()