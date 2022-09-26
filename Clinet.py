#!/usr/bin/python3
import socket
import sys
import time
import datetime
def OPTIONS():
    # OPEN是正转动 CLOSE是反转 Q是断开与服务器的连接 D是将远控设备踢下线
    # OPEN is positive rotation CLOSE is reverse rotation Q is disconnection from the server D is disconnection of the remote control device
    CS = input("\n-----#(OPEN||CLOSE|Q|D)>>>")
    return CS
def main(MoteIP,MotePort):
    SOCKS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCKS.connect((MoteIP, MotePort))
    print("[+]正在接入远程主机")
    print(SOCKS.recv(1024).decode())
    while True:
        CS = OPTIONS()
        if "OPEN" in CS:
            SOCKS.send(b'HACK') # o 6F # c 63

            print("[+]发送运行指令成功!")
        elif "CLOSE" in CS:
            SOCKS.send(b'STOP')  # o 6F # c 63

            print("[+]发送停止指令成功!")
        elif "Q" in CS:
            SOCKS.send(b'EXIT')

            print("[-]准备关闭会话")
            print("[+]服务器返回了一条消息:",SOCKS.recv(1024).decode())
            sys.exit(0)
        elif "D" in CS:
            SOCKS.send(b'DEV')
            print("[-]准备远程关闭设备")
            print("[+]服务器返回了一条消息:", SOCKS.recv(1024).decode())
        else:
            continue
        print("[+]服务器返回了一条消息:", SOCKS.recv(1024).decode())
if __name__ == '__main__':

    main("Enter the server IP here",int(10031))

