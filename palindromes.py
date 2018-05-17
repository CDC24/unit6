#Caleb Callaway
#5/16/18
#homework6Tests.py - four homework programs

file=open("engmix.txt")
"""
i=0
for line in file:
    while i <20:
        line = line.strip()
        L = []
        for letter in line:
            L.append(letter)
        NewL = L[:]
    print(NewL[].reverse)
    i+=1
"""
i = 0
for line in file:
    while i<10:
        line = line.strip()
        reverse = ""
        for ch in line:
            reverse = ch+reverse
        if reverse = line:
            print (reverse)
        i += 1