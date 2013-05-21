from random import randint
import os
import sys


def create_random():
    """Create a file with random number for user"""


    name = raw_input("Enter filename to output: ")
    pwd = name + ".txt"
    if os.path.exists(pwd):
        print "Error, user already exists."
        sys.exit(-1)
    r = str(randint(0, 999))
    d = open(pwd, "w")
    d.write("You number to skey.exe is: %s" %r)
    d.close()
    
    sys.exit(-1)
    
if __name__ == "__main__":
    while True:
        create_random()
        action = raw_input("Enter action ((c)create or (q)uit): ")
        if action == "c":
            create_random()
        elif action == "q":
            sys.exit(0)