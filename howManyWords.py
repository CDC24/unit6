#Caleb Callaway
#5/10/18
#howManyWords.py - print the number of words for each number of letters



file=open("engmix.txt")


1s = 0
2s = 0
3s = 0
4s = 0
5s = 0
6s = 0
7s = 0
8s = 0
9s = 0
10s = 0
11s = 0
12s = 0
13s = 0
14s = 0
15s = 0
16s = 0
17s = 0
18s = 0
19s = 0
20s = 0
21s = 0

for word in file:
    for i in range (0,21):
        if len(word)==i:
            (i,"s")+=1
    
