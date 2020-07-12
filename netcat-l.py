#!/usr/bin/env python3

'''
Onno de Gouw
Stefan Popa
'''

import socket

def handlestring(datastring, length, delimiter):
    stringlist = datastring.split(sep=delimiter)
    filteredlist = []

    for string in stringlist:
        filteredlist.append(string[length:])
        filteredstring = delimiter.join(filteredlist)

    return filteredstring

def handle(sock):

    while 1:
        data, addr = sock.recvfrom(size)
        
        if not data:
            break
        
        if data:
            datastring = data.decode("utf-8")
            sock.sendto("Message receieved!".encode("utf-8"), addr)
            print(handlestring(datastring, len("spam "), "\n"))
     

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    handle(s)
    s.close()

if __name__ == "__main__":
    host = "localhost"
    port = 42424
    size = 65535
    main()
