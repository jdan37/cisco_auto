#!/usr/bin/env python3

def main():
    netcls()
    biny()
    #subn()


def netcls():
    oc1 = int(input("Enter first octet: "))
    oc2 = int(input("Enter sec octet: "))
    oc3 = int(input("Enter third octet: "))
    oc4 = int(input("Enter fourth octet: "))
    r = ""

    if oc1 <= 126:
        r = "A"
    elif oc2 <= 191:
        r = "B"

    elif oc3 <= 223:
        r = "C"

    print('{}.{}.{}.{} is a class {} address'.format(oc1, oc2, oc3, oc4, r))

def ciderNote():
    maskoc1 = 255
    maskoc2 = 255
    maskoc3 = 255
    maskoc4 = 0


    if  maskoc1 <= 126:
        r = "A"
    elif oc2 <= 191:
        r = "B"

    elif oc3 <= 223:
        r = "C"


def biny(dec):
    #dec = int(input("Enter number"))

    if dec >= 128:
        oc8 = 1
        dec = dec - 128
    else:
        oc8 = 0
    if dec >= 64:
        oc7 = 1
        dec = dec - 64
    else:
        oc7 = 0
    if dec >= 32:
        oc6 = 1
        dec = dec - 32
    else:
        oc6 = 0
    if dec >= 16:
        oc5 = 1
        dec = dec - 16
    else:
        oc5 = 0
    if dec >= 8:
        oc4 = 1
        dec = dec - 8
    else:
        oc4 = 0
    if dec >= 4:
        oc3 = 1
        dec = dec - 4
    else:
        oc3 = 0
    if dec >= 2:
        oc2 = 1
        dec = dec - 2
    else:
        oc2 = 0
    if dec >= 1:
        oc1 = 1
        dec = dec - 1
    else:
        oc1 = 0

    #print('Binary: {}{}{}{}{}{}{}{}'.format(oc8, oc7, oc6, oc5, oc4, oc3, oc2, oc1))
    return oc8, oc7, oc6, oc5, oc4, oc3, oc2, oc1



def subn():
    dec = int(input("Enter number"))
    x = biny(dec)
    print(type(x),x)



if __name__ == '__main__':main()

