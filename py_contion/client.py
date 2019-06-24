#!/usr/bin/env python
# coding=utf-8
import socket
import time

def Client():
    sock=socket.socket(socket,AF_INET,socket.SOCK_STREAM)
    sock=sock.connect(('127.0.0.1', 8888))
    time.sleep(2)
    sock.send('1')
    print sock.recv(1024)
    sock.close()

if __name__=='__name__':
    Client()
