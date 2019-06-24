#!/usr/bin/env python
# coding=utf-8
import socket
def Server():
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8888));
    sock.listen(1)
    while True:
        connection,address=sock.accept()
        try:
            connection.settimeout(1)
            buf=connection.recv(1024)
            if buf=='1':
                connection.send('welcome to server!')
            else:
                connection.send('Goodbye!')
        except socket.timeout:
            print 'socket timeout'
        connection.close()

if __name__=='__main__':
    Server()
