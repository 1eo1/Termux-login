#!$PREFIX/bin/env python

import getpass
import hashlib
import sys
import os

password = getpass.getpass(prompt='| ')

filepass = open("/data/data/com.termux/files/.pass", "r")
filepass = filepass.read().split("\n")[0]

password = password.encode()
password = hashlib.sha256(password).hexdigest()

if password != filepass:
    print("")
    os.system("exit")
else:
    prefix = "/data/data/com.termux/files/usr"
    home = "/data/data/com.termux/files/home"
    motd = False
    hush = False

    os.system("clear")

    try:
        open(prefix + "/etc/motd")
        motd = True
    except:
        motd = False

    try:
        open(home + "/.hushlogin")
        hush = True
    except:
        hush = False

    if motd and not hush:
        print(open(prefix + "/etc/motd").read())
    
    os.system(sys.argv[1] + " " + sys.argv[2])
