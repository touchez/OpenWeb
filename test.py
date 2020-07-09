# coding=UTF-8
import serial
import pynmea2
import socketio
import time

# socket_server_ip = "http://192.168.2.137:9099?userId=树莓派1号"
socket_server_ip = "http://touchez.cn:9099?userId=医疗端"

sio = socketio.Client()

@sio.on('openweb')
def on_open(data):
    print("openweb收到消息" + data)
    openWeb("http://47.115.145.148:10080/doctor.html")

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.on('messageevent')
def on_msg(data):
    print("get msg:" + data)

sio.connect(socket_server_ip)