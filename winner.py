#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "w")  # File di output fornito dalla piattaforma

def less_time(submissions, el):
    player = el[0]
    n_challenge = el[1]
    flag = el[2]
    time = el[3]
    min = el[3]
    for i in submissions:
        if player == i[0] and n_challenge == i[1] and flag == i[2] and min > i[3]:
            min = i[3]
    if min == time:
        return True
    
    return False

def calcola_classifica(M, N, S, tasks, submissions):
    # SCRIVI QUA IL TUO CODICE
    info = []
    for i in range(M):
        info.append({"id": i,
                     "points": 0,
                     "time": 0,
                     "challenge":  []})
    

    for i in submissions:
        player = i[0]-1
        if less_time(submissions, i) and (info[player]["id"] == player) and (i[2] == tasks[i[1]-1][0]) and not(i[2] in info[player]["challenge"]):
            info[player]["challenge"].append(i[2])
            
            info[player]["points"] += tasks[i[1]-1][1]
            
            if info[player]["time"] < i[3]:
                info[player]["time"] = i[3]
                


    results = []
    temp = []
    for i in range(M):
        results.append([info[i]["points"], info[i]["time"], info[i]["id"]])


    results = sorted(results, key=lambda x: (x[0], -x[1]), reverse=True)


    for i in results:
        print(f"{i[2]+1} {i[0]}", file=fout)

    print(results)

#M = n_player
#N = n_task
#S = tot_submission
M, N, S = map(int, fin.readline().strip().split())
tasks = []
submissions = []

for _ in range(N):
    tid, flag, points = fin.readline().strip().split()
    tasks.append((flag, int(points)))

for _ in range(S):
    player, task, submitted, timestamp = fin.readline().strip().split()
    submissions.append((int(player), int(task), submitted, int(timestamp)))

calcola_classifica(M, N, S, tasks, submissions)
