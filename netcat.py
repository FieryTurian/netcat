#!/usr/bin/env python3

'''
Onno de Gouw 
Stefan Popa
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

stringbuf = ""
for i in range (0, 1000):
    stringbuf = stringbuf + "spam " + str(i) + "\n"
buf = stringbuf.encode("utf-8")

s.sendto(buf, ("localhost", 42424))

while 1:
    reply, addr = s.recvfrom(65535)
    
    if reply:
        msg = reply.decode("utf-8")
        print(msg)
        break
        
    if not reply:
        s.sendto(buf, ("localhost", 42424))
        
s.close()
