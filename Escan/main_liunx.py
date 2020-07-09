#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
#import _thread
from time import sleep
from prettytable import PrettyTable
from scapy.all import ARP,TCP,IP,sr1
from threading import Thread
os.system('')

class mainl():
 def run():
      if data['pattern'] == '0':
         def aaa(ip):
   
          a = ARP(pdst=ip)
          b = sr1(a,verbose=False,timeout=3,iface=data['we'])
          if b :
       
            mac = b.hwsrc
            datd.append(ip)
            datb[ip] = mac
            #print(f'{ip} -- {mac}')
          #else :
           #  print(f'{ip} NO') 
         datb = {}
         datd = []
         
         print('\033[36m[O] 开始扫描,正在扫描中...\033[0m')
         for i in range(255):
           ip = data['wip'] + str(i)
           #_thread.start_new_thread(aaa,(ip,))
           #aaa(ip)
           t = Thread(target=aaa, args=(ip,))
           t.start()
           sleep(0.008)
         if data['time'] == '01o':
             sleep(6)
         else:
             sleep(int(data['time']))
         print('\033[36m[O] 扫描己结束,打印出扫描结果...\033[0m')
         tb = PrettyTable()
         tb.field_names = ["ip", "mac"]
         for i in range(len(datb)):
              tb.add_row([datd[i],datb[datd[i]]])
         print(tb) 
      elif data['pattern'] == '1':
          def ccc(xx_ip,i):
              a = IP(dst=xx_ip)/TCP(dport=int(i),flags='S')
              b = sr1(a,verbose=False,timeout=1,iface=data['we'])
              #print(b.show()) 
              if  b  != None:
               if  b[TCP].flags == 'SA' :
                   datb.append(str(i))
                   #print(str(i) +'OPEN')
               #else:
                #   print(str(i) +'NO' )
          def  bbb(xx_ip):
                 a = ARP(pdst=xx_ip)
                 b = sr1(a,verbose=False,timeout=2)
                 if b :
                    print('\033[36m[O] 开始扫描,正在扫描中...\033[0m')
                    #print(int(data['comes'])+1)
                    for i in range(1,int(data['comes'])+1):
                       t = Thread(target=ccc, args=(xx_ip,int(i)))
                       t.start()
                       sleep(0.0001)
                    
                 else:
                     print('\033[31m[X] E: ip XX??\033[0m')
                     fe = 1
          datb = []
          fe = 0  
          bbb(data['xx_ip'])
          if fe == 0:
           if data['time'] == '01o':
                #print(325)
                sleep(10)
           else:
             #print(int(data['time']))
             sleep(int(data['time']))
           print('\033[36m[O] 扫描己结束,打印出扫描结果...\033[0m')
           tb = PrettyTable()
           tb.field_names = ["port", "zuantia"]
           #print(datb)
           for i in range(len(datb)):
              tb.add_row([datb[int(i)],'OPEN'])
           print(tb)     
          
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
                
                  mainl.run()
               
      elif d == "show": 
              if data['pattern'] == '0':
                 tb = PrettyTable()
                 tb.add_column('必需的',['模式(ip or port)','网卡','所属网段特定的ip段','time'])
                 tb.add_column('name',['pattern','we','wip','time'])
                 tb.add_column('vlue',[data['pattern'],data['we'],data['wip'],data['time']])
                 print(tb)
                 
              elif data['pattern'] == '1':
                 tb = PrettyTable()
                 tb.add_column('必需的',['模式(ip or port)','目标ip','some','网卡','time'])
                 tb.add_column('name',['pattern','xx_ip','comes','we','time'])
                 tb.add_column('vlue',[data['pattern'],data['xx_ip'],data['comes'],data['we'],data['time']])
                 print(tb)
      else:
           print('\033[31m[X] E:?? input ??\033[0m')           
 def scanf():
  cf = 0
  global data
  data = {'pattern':'0','wip':'例:192.168.1.','xx_ip':'','comes':'65535','we':'eth0','time':'01o'}
  while cf == 0:
   d = input('RPG Intranet_Penetration(\033[31mEth_scan\033[0m)>')
   if d :
    mainl.jan(d)
   else:
    print('\033[31m[X] E:input ??\033[0m')
    
def main():
 mainl.scanf()   

main()