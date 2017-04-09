#! /usr/bin/python3.4
import soundcloud
import os
from shutil import *

client_id = "F4GaA9l45LjxV77qgsQ75tzRmC0MJFHu"
client = soundcloud.Client(client_id=client_id)

print("DATA BASE EDITOR FOR VLC_interface")
print("==================================")
add = input("add : ")
if add[0:23] == "https://soundcloud.com/":
    file = open("/home/pi/Remi/Chaine/SoundCloud.txt","a")
    f = client.get("/resolve",url=add)
    file.write(add+";"+f.title+"\n")
    print(f.title+" : added")
    file.close()
else:
    name = input("name : ")
    file = open("/home/pi/Remi/Chaine/Radio.txt","a")
    file.write(add+";"+name+"\n")
    file.close()
