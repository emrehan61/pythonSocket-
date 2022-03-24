import socket
import requests
import sys
import os
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind(('127.0.0.1', 1453))
s1.listen(5)
onl = []
url = 'https://yfapi.net/v7/finance/options/'
querystring = {""}

headers = {
    'x-api-key': ""}

# onl = list to hold online users on server


def menu():
    s = ""
    while s != "q":
        s = input("what to do:  ")
        if s == "a":
            addUser()
        elif s == "r":
            usDel = input("delete an user")
            if usDel in onl:
                removeUser(usDel)
            else:
                print("Couldn't find user")
                continue
        elif s == "q":
            sys.exit("Quitting")
        else:
            continue


def state():
    ins = 0
    apiHeader = ""
    responseSocket, adress = s1.accept()
    responseSocket.send("First Message is Succesful ".encode("UTF-8"))
    while True:

        print(f"Connected to adress: {adress} ")
        try:
            msg = responseSocket.recv(1024).decode("utf-8")
            print(msg)
            if(msg == "empty"):
                responseSocket.send("empty".encode("utf-8"))

            if ins == 0:
                responseSocket.send("API".encode("utf-8"))
                try:
                    apiHeader = responseSocket.recv(1024).decode("utf-8")
                    headers['x-api-key'] = apiHeader
                    print("got your api header")
                    ins += 1

                except ConnectionError:
                    responseSocket.close()
                    print("unable to get api key")
                    break
            if "symbol: " in msg:
                url2 = ""
                temps = msg[8:]
                url2 = url + temps
                print(temps)
                print(msg)
                print("sss")
                print(url2)
                response = requests.request(
                    "GET", url2, headers=headers)
                responseSocket.send(response.text.encode("utf-8"))
            else:
                #    responseSocket.recv(1024).decode("utf-8")
                pass

        except ConnectionError:
            print("Connection failed ude to server")
            print(f"mesage from the client is: {msg}")
            break
            responseSocket.close()


def addUser():
    x = input("enter your user name: ")
    if x not in onl:
        onl.append(x)

        os.system("start cmd /k python mclient.py")
        state()

        # şimdilik isime gerek yok,
        # fikir olarak mclient a bir tane getName methodu koyup buraya sendleyip,
        # eğer receive getName olarak bir girdi algılarsa geri client a
        # username i sendle

    else:
        print("user already exist")


def removeUser(s):
    if s in onl:
        onl.remove(s)
    else:
        print("there is no such user")


menu()
