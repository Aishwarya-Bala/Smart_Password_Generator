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

def Rule1(passwd):
    '''
    Alternate Characters Increment Decrement
    Example - hello -> idmkp
    '''
    debug("Rule1")
    new_pass = ""
    for i in range(len(passwd)):
        if(i % 2 == 0):
            new_pass += getNextChar(passwd[i], True)
        else:
            new_pass += getNextChar(passwd[i], False)
    debug(new_pass)
    debug("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    return new_pass

def Rule2(passwd):
    '''
    Take successive character of every character
    Example - hello -> ifmmp
    '''
    debug("Rule2")
    new_pass = ''.join(list(map(lambda x: getNextChar(x, True), list(passwd))))
    debug(new_pass)
    debug("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    return new_pass

def Rule3(passwd):
    '''
    Take previous character of every character
    Example - hello -> gdkkn
    '''
    debug("Rule3")
    new_pass = ''.join(list(map(lambda x: getNextChar(x, False), list(passwd))))
    debug(new_pass)
    debug("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    return new_pass


def Rule4(passwd):
    '''
    Take successive character of every alternate character
    Example - hello -> iemlp
    '''
    debug("Rule4")
    def f(i):
        if(i % 2 == 0):
            return getNextChar(passwd[i], True)
        else:
            return passwd[i]

    new_pass = ''.join([f(i) for i in range(len(passwd))])
    debug(new_pass)
    debug("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    return new_pass

def Rule5(passwd):
    '''
    Take previous character of every alternate character
    Example - hello -> gekln
    '''
    debug("Rule5")
    def f(i):
        if(i % 2 == 0):
            return getNextChar(passwd[i], False)
        else:
            return passwd[i]
    new_pass = ''.join([f(i) for i in range(len(passwd))])
    debug(new_pass)
    debug("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    return new_pass

def Rule6(passwd):
    '''
    Take successive character of every character at position
    indicated by your random number sequence
    '''
    debug("Rule6")
    my_seq = []
    for i in seq:
        my_seq.append(i % len(passwd))

    def f(i):
        if(i + 1 in my_seq):
            return getNextChar(passwd[i], True)
        else:
            return passwd[i]

    new_pass = ''.join([f(j) for j in range(len(passwd))])
    debug(new_pass)
    debug("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    return new_pass

def Rule7(passwd):
    '''
    Take previous character of every character at position
    indicated by your random number sequence
    '''
    debug("Rule7")
    my_seq = []
    for i in seq:
        my_seq.append(i % len(passwd))
    def f(i):
        if(i + 1 in my_seq):
            return getNextChar(passwd[i], False)
        else:
            return passwd[i]
    new_pass = ''.join([f(i) for i in range(len(passwd))])
    debug(new_pass)
    debug("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    return new_pass

def Rule8(passwd):
    '''
    Replace characters at even places by a particular symbols/alphabets/number - Easy
    Example - hello ->  h@l@o  (Replacing even places by symbol @)
    '''
    debug("Rule8")
    '''
    p = list(passwd)
    p[::2] = [symbol] * (len(passwd)//2)
    new_pass = ''.join(p)
    '''
    new_pass = ""
    for i in range(len(passwd)):
        if(i % 2 == 0):
            new_pass += symbol
        else:
            new_pass += passwd[i]
    debug(new_pass)
    debug("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    return 