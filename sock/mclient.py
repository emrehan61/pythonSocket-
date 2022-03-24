import socket
import sys
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect(('127.0.0.1', 1453))
s1.send("Connection Succesful!!".encode("utf-8"))


def state():
    apigot = 0
    while True:
        apigot += 1
        try:
            s2 = s1.recv(1024).decode("utf-8")
            print(s2)
            if s2 == "API":

                try:
                    apKey = input("enter your api key")
                    # OTklWCC4089UKomFygJjph3LAVAO1c25loQ4GvIb my api key with only for 300 requests
                    s1.send(apKey.
                            encode("utf-8"))
                    apigot += 1

                except:
                    print("error")
            if apigot > 2:

                s = input("\n op: ")
                if s == "s":
                    s = input("give me the symbol: ")
                    print(s2)
                    s2 = "symbol: " + s
                    print(s2)
                    s1.send(s2.encode("utf-8"))
                if s == "q":
                    sys.exit("Quitting")
                else:
                    s1.send("empty".encode("utf-8"))
                    continue

        except:
            print("connection failed")
            s1.close()
            break


def askForSymbol():

    s = input("choose symbol to be listed ")
    s1.send(s.encode("utf-8"))


state()
