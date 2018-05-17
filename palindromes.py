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

reverse = ""
for line in file:
    line = line.strip()
    while i <100:
        for ch in line:
    reverse = ch+reverse
print (reverse)