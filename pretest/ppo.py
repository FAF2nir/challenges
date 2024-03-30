#!/bin/env python3

import sys
from string import *

# Se vuoi leggere/scrivere da file decommenta qua
fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "w")  # Output da inviare alla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
#fin = sys.stdin  # input fornito dalla piattaforma
#fout = sys.stdout  # Output da inviare alla piattaforma

digits = "1234567890"
special = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def check1_2(n):
    return len(n)>=8 and len(n)<=16

def check3(n):
    lower = False
    upper = False
    for el in n:
        if el.isupper():
            upper = True
        if el.islower():
            lower = True
    
    return (upper and lower)

def check4(n):
    return (any(el in digits for el in n) and any(el in special for el in n))

def check5(n):
    return (not any(n[i] == n[i+1] for i in range(len(n)-1)))

def check6(o, n):
    for i in range(len(o)-1):
        if n == (o[:i] + o[i+1:]):
            return False

    if abs(len(o) - len(n)) == 0:
        for i in range(len(o)-1):
            if (n[:i] + n[i+1:]) == (o[:i] + o[i+1:]):
                return False

    for i in range(len(o)-1):
        if o == (n[:i] + n[i+1:]):
            return False
    
    return True


def controlla(n, o):
    if check1_2(n) and check3(n) and check4(n) and check5(n) and check6(o, n):
        return 1

    return 0


N = int(fin.readline().strip())

for _ in range(N):
    nuova, vecchia = fin.readline().strip().split(" ")
    print(controlla(nuova, vecchia), file=fout)

