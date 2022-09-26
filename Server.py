#!/usr/bin/python3
# @ Martin
import socket
import sys
import time
import datetime
import threading
DEV_SOCK_AND_USERNAME_PORT = list()
HCK_SOCK_AND_USERNAME_PORT = list()
mutex = threading.Lock()
def SOCK_Dev(PORT):
    global DEV_SOCK_AND_USERNAME_PORT,HCK_SOCK_AND_USERNAME_PORT
    MIAN_DEV_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    MIAN_DEV_SOCK.bind(("", PORT))
    MIAN_DEV_SOCK.listen(1)
    while True:
        print(f"[*]Waiting for remote device connection...\033[4;33m{PORT}\033[0m")
        DEV_SOCKET, DevIP = MIAN_DEV_SOCK.accept()
        print(f"[\033[34m+\033[0m]Device \033[32m{DevIP[0]}\033[0m:\033[4;33m{DevIP[1]}"
              f"\033[0m ---------- [\033[32mOnline\033[0m]-[\033[4;33m{PORT}\033[0m]")
        DEV_SOCK_AND_USERNAME_PORT.append(DEV_SOCKET)
        DEV_SOCK_AND_USERNAME_PORT.append(DevIP[0])
        DEV_SOCK_AND_USERNAME_PORT.append(DevIP[1])
        while True:

            try:
                DEV_SOCKET.send(b'x')
            except:
                break
            else:
                time.sleep(5)
        DEV_SOCK_AND_USERNAME_PORT.remove(DEV_SOCKET)
        DEV_SOCK_AND_USERNAME_PORT.remove(DevIP[0])
        DEV_SOCK_AND_USERNAME_PORT.remove(DevIP[1])

def Get_DATA(SOCK,Name,Mote):

    DATA = SOCK.recv(1024).decode()
    if len(DATA) <= 0:
        if Mote == 0:
            print(f"[\033[34m-\033[0m]\033[32m{Name}\033[0m ---------- [\033[32mOffline\033[0m]")
        else:
            print(f"[\033[34m-\033[0m]\033[31m{Name}\033[0m ---------- [\033[32mOffline\033[0m]")
        return 0
    return DATA

def SOCK_Hacker(PORT):
    global DEV_SOCK_AND_USERNAME_PORT,HCK_SOCK_AND_USERNAME_PORT
    MIAN_HACK_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    MIAN_HACK_SOCK.bind(("", PORT))
    MIAN_HACK_SOCK.listen(1)
    while True:
        print(f"[*]Waiting for the controller to connect...\033[4;33m{PORT}\033[0m")
        HACK_SOCKET, Hacker_IP = MIAN_HACK_SOCK.accept()
        print(f"[\033[34m+\033[0m]Controller \033[31m{Hacker_IP[0]}\033[0m:\033[4;33m{Hacker_IP[1]}"
              f"\033[0m ---------- [\033[32mOnline\033[0m]-[\033[4;33m{PORT}\033[0m]")
        HACK_SOCKET.send(b"[+]Server Connect You !")

        HCK_SOCK_AND_USERNAME_PORT.append(HACK_SOCKET)
        HCK_SOCK_AND_USERNAME_PORT.append(Hacker_IP[0])
        HCK_SOCK_AND_USERNAME_PORT.append(Hacker_IP[1])

        #HCK_SOCK = HACK_SOCKET
        while True:

            DATA = Get_DATA(HACK_SOCKET, Hacker_IP[0],1)
            mutex.acquire()
            if DATA != 0:
                if 'EXIT' in DATA:
                    HACK_SOCKET.send("Socket Cloese-----[Success]".encode())
                    HCK_SOCK_AND_USERNAME_PORT[0].close()

                    print(f"[\033[34m-\033[0m]Hacker SOCKET 已被关闭")
                    break
                elif 'DEV' in DATA:
                    DEV_SOCK_AND_USERNAME_PORT[0].send(b'y')
                    HACK_SOCKET.send("Device Cloese Socket-----[Success]".encode())
                if DEV_SOCK_AND_USERNAME_PORT:
                    HACK_SOCKET.send(f"Device----[Online]\r\n".encode())
                    now = datetime.datetime.now()
                    print(
                        f"\033[31m{Hacker_IP[0]}\033[0m ==> \033[32m{DEV_SOCK_AND_USERNAME_PORT[1]}\033[0m ---------- [\033[32mOK\033[0m]  %s" % (
                            now.strftime("%Y-%m-%d %H:%M:%S")))
                    if 'HACK' in DATA:

                        DEV_SOCK_AND_USERNAME_PORT[0].send(b'o')

                        HACK_SOCKET.send(f"Server Send {DEV_SOCK_AND_USERNAME_PORT[1]} RUN Command !!Success!!".encode())
                        print(f"Runing----------[\033[32mOK\033[0m]")
                    elif 'STOP' in DATA:

                        DEV_SOCK_AND_USERNAME_PORT[0].send(b'c')

                        HACK_SOCKET.send(f"Server Send {DEV_SOCK_AND_USERNAME_PORT[1]} STOP Command !!Success!!".encode())
                        print(f"Stoping----------[\033[32mOK\033[0m]")

                else:
                    HACK_SOCKET.send(f"Device----[OffLine]".encode())
                mutex.release()
            else:
                HACK_SOCKET.close()
                mutex.release()
                break

        HCK_SOCK_AND_USERNAME_PORT.remove(HACK_SOCKET)
        HCK_SOCK_AND_USERNAME_PORT.remove(Hacker_IP[0])
        HCK_SOCK_AND_USERNAME_PORT.remove(Hacker_IP[1])





def main():
    Hacker = threading.Thread(target=SOCK_Hacker,args=(10031,))
    Device = threading.Thread(target=SOCK_Dev,args=(10030,))
    Hacker.start()
    Device.start()


if __name__ == '__main__':
    main()