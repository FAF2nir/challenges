#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "w")  # Output da inviare alla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
#fin = sys.stdin  # input fornito dalla piattaforma
#fout = sys.stdout  # Output da inviare alla piattaforma

def moves(N, V):
    V2 = sorted(V)
    ans = 0

    for i in range(N):
        if V[i] != V2[i]:
            ans += 1
    
    return max(0, ans-1)


N = int(fin.readline().strip())
V = list(map(int, fin.readline().strip().split(" ")))
print(moves(N, V), file=fout)