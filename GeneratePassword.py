import math
import random
import os
import datetime
from entropy import PasswordStrength

seq = []
times = 2
symbol = '#'
dt = None

# Set this variable to True if wanna debug
DEBUG = False

seed = os.getpid()
random.seed(seed)

def print_sequence(l):
    for i in l:
        print(l, end = "\t")
        print()

def debug(smth):
    if(DEBUG):
        print(smth)

def gimme_special_symbol():
    special_symbols = list(range(33, 48))
    special_symbols.extend(list(range(58, 65)))
    special_symbols.extend(list(range(91, 95)))
    special_symbols.extend(list(range(123, 127)))
    #debug("Special symbols : " + str(special_symbols))
    debug("No. of special symbols = " + str(len(special_symbols)))
    x = special_symbols[random.randint(0, (len(special_symbols) - 1))]
    debug("x = " + str(x))
    return chr(x)


def getNextChar(c, forward):
    if(c.isalpha()):
        if(forward):
            if(ord(c) in list(range(65, 91))):
                if((ord(c) + 1) > 90):
                    return chr(65)
            elif(ord(c) in list(range(97, 123))):
                if((ord(c) + 1) > 122):
                    return chr(97)
            return(chr(ord(c) + 1))
        else:
            if(ord(c) in list(range(65, 91))):
                if((ord(c) - 1) < 65):
                    return chr(90)
            elif(ord(c) in list(range(97, 123))):
                if((ord(c) - 1) < 97):
                    return chr(122)
            return(chr(ord(c) - 1))
    elif(c.isdigit()):
        if(forward):
            return str((int(c) + 1) % 10)
        else:
            if(int(c) - 1 > 0):
                return str((int(c) - 1))
            return(str(9))
    return(c)


import string
digs = string.digits + string.ascii_letters

