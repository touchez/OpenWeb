#!/usr/bin/python3
# coding:utf-8

import socket
import time
import sys
import threading
import re
from OpenWeb import openWeb

HOST_IP = ""
HOST_PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind((HOST_IP, HOST_PORT))
s.listen(5)
print('Waiting for connection...')

urlPattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome To OpenWeb Server!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        uft8Data = data.decode('utf-8')
        if not data or uft8Data == 'exit':
            break
        url = re.findall(urlPattern, data.decode('utf-8'))
        if url:
            print('received message ' + uft8Data + ' have url : ')
            print(url)
            openWeb(url[0])
            sock.send(('Open %s in webbrowse successfully!' % uft8Data).encode('utf-8'))
        else:
            print('received message ' + uft8Data + ' haven\'t url')
            sock.send(('%s doesn\'t contain a valid url! PLEASE SEND NEW ONE！' % uft8Data).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()