import sys
import copy

# Se vuoi leggere/scrivere da file decommenta qua
fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "w")  # Output da inviare alla piattaforma

def not_empty_neigh(n, V):
    N_empty_cells = 0
    for i in n:
        if V[i[0]][i[1]] != '.':
           N_empty_cells += 1
            
    return N_empty_cells

def round(N, M, K, V):
    V2 = copy.deepcopy(V)
    neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                            for y2 in range(y-1, y+2)
                            if (-1 < x <= N and
                                -1 < y <= M and
                                (x != x2 or y != y2) and
                                (0 <= x2 < N) and
                                (0 <= y2 < M))]
    
    for _ in range(K):
        for i in range(N):
            for j in range(M):
                
                if (V[i][j] == "." and (not_empty_neigh(neighbors(i, j), V) > 4)):
                    V2[i][j] = "+"
                elif(V[i][j] == "+" and (not_empty_neigh(neighbors(i, j), V) > 4)):
                    V2[i][j] = "*"
                elif(V[i][j] == "+" and (not_empty_neigh(neighbors(i, j), V) < 4)):
                    V2[i][j] = "."
                elif(V[i][j] == "*" and (not_empty_neigh(neighbors(i, j), V) > 4)):
                    V2[i][j] = "+"
                elif(V[i][j] == "*" and (not_empty_neigh(neighbors(i, j), V) < 4)):
                    V2[i][j] = "."

        V = copy.deepcopy(V2)


    for v in V2:
        print("".join(v), file=fout)

(N, M, K) = map(int, fin.readline().strip().split())
V = []
for i in range(N):
    V.append(list(fin.readline().strip()))

round(N, M, K, V)