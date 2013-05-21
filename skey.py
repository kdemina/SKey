#!/usr/bin/python
 
 
from md5 import md5
import sys, os
from random import randrange
 
def skey_register():
    """ Creare keys for new user"""
    name = raw_input("Enter your name: ")
    pwd = name + ".txt"
    if os.path.exists(pwd):
        print "Error, user already exists."
        sys.exit(-1)
    r = raw_input("Enter your secrete number: ")
    new_name = name + "Keys.txt"
    d = open(new_name, "w")
    for i in range(100):
        r = md5(r).hexdigest()
        k = str(i) + " " + r
        d.write("%s\n" % (k))
    d.close()
    key = md5(r).hexdigest()
    try:
        f = open(pwd, "w")
        print "Your keys are created"
    except:
        print "error!"
        sys.exit(-1)
    f.write(key)
    f.close()
 
def skey_login():
    """Login the user, if he pass the authentication"""
    name = raw_input("Enter your name: ") + ".txt"
    try:
        f = open(name, "r")
    except:
        print "error!"
        sys.exit(-1)
    passwd = f.read()
    f.close()
    upasswd = raw_input("Enter password: ")
    new_upasswd = md5(upasswd).hexdigest()
    if new_upasswd != passwd:
        print "Invalid password!"
    else:
        print "Login successful!"
        f = open(name, "w")
        f.write(upasswd)
        f.close()
 
if __name__ == "__main__":
    while True:
        action = raw_input("Enter action ((r)egister, (l)ogin or (q)uit): ")
        if action == "r":
            skey_register()
        elif action == "l":
            skey_login()
        elif action == "q":
            sys.exit(0)
