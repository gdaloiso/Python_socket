#!/usr/bin/python3
import socket               
s = socket.socket()         
host = socket.gethostname() 
port = 55555                
s.bind((host, port))        
s.listen(5)                 
while True:
    c, addr = s.accept()     
    print ('Got connection from', addr)
    c.send(b'Thank you for connecting')
    data = c.recv(1024)
    if data: print (data)
    c.close()               