#!/usr/bin/python3
import socket
s = socket.socket()         
host = socket.gethostname() 
port = 55555                
s.connect((host, port))
data = s.recv(1024)
if data: print (data)
msg = input("Enter message: ")
s.send(msg.encode())
s.close                    