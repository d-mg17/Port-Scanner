#!/usr/bin/env python

import socket
import subprocess
import sys
import os
from datetime import datetime


def main():
    """Cleanning the terminal screen, saving user input and saving host IP & running typeOfScan function"""
    os.system("clear")
    print("-" * 65)
    print("Welcome to port scanner")
    input("Press ENTER to continue... (or CTRL + C to exit")

    typeOfScan = input(
        "Do you want to do a fast scan or a deep scan of hosts? (fast/deep) >"
    )
    typeOfScan = typeOfScan.lower().strip()
    typeOfScan(typeOfScan=typeOfScan)


def typeOfScan(typeOfScan):
    if typeOfScan == "fast":
        try:
            remoteServer = input("Enter host name to scan: >")
            remoteServerIP = socket.gethostbyname(remoteServer)

            banner(serverIP=remoteServerIP, serverName=remoteServer)
            fastScan(serverIP=remoteServerIP)

        except KeyboardInterrupt:
            print("Closing programm...\n")
            sys.exit()
        except socket.gaierror:
            print("Hostname could not be resolved.\nRestarting programm...")
            main()

    elif typeOfScan == "deep":
        try:
            remoteServer = input("Enter host name to scan: >")
            remoteServerIP = socket.gethostbyname(remoteServer)

            banner(serverIP=remoteServerIP, serverName=remoteServer)
            deepScan(serverIP=remoteServerIP)

        except KeyboardInterrupt:
            print("Closing programm...\n")
            sys.exit()
        except socket.gaierror:
            print("Hostname could not be resolved.\nRestarting programm...")
            main()
    else:
        print("Wrong input.\nRestarting programm...")
        main()


def banner(serverIP, serverName):
    """Printing banner with information about the host"""
    print("-" * 65)
    print(f" Scanning ports of: {serverName} with IP: {serverIP}")
    print("-" * 65)


def fastScan(serverIP):
    """Doing fast scan of ports, around 12 ports"""
    portsToCheck = [20, 21, 22, 139, 137, 445, 53, 223, 80, 8080, 8443, 23, 25, 69]
    try:
        scanner(portsToCheck=portsToCheck, serverIP=serverIP)
    except KeyboardInterrupt:
        print("Closing programm...\n")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.\nRestarting...")
        main()


def deepScan(serverIP):
    """Doing deep scan of ports, around 20 ports"""
    portsToCheck = [
        20,
        21,
        22,
        139,
        137,
        445,
        53,
        223,
        80,
        8080,
        8443,
        23,
        25,
        69,
        110,
        143,
        993,
        995,
        3306,
        3389,
        5900,
        5901,
        5902,
        5903,
        5904,
        5905,
    ]
    try:
        scanner(portsToCheck=portsToCheck, serverIP=serverIP)
    except KeyboardInterrupt:
        print("Closing programm...\n")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.\nRestarting...")
        main()


def scanner(portsToCheck, serverIP):
    """Doing port scan and then printing time of scan"""
    portsToCheck = portsToCheck
    startingTime = datetime.now()
    try:
        for port in portsToCheck:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((serverIP, port))
            if result == 0:
                print(f"Port {port} = {socket.getservbyport(port)}:          Open")
            sock.close()

    except KeyboardInterrupt:
        print("Closing programm...\n")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.\nClosing programm...")
        sys.exit()

        # Checking finished time in order to compare
        finishedTime = datetime.now()
        print("Scanning completed in: ", startingTime - finishedTime)


if __name__ == "__main__":
    main()
    return 0
