#Caleb Callaway
#5/16/18
#homework6Tests.py - four homework programs

file=open("engmix.txt")

i=0
for line in file:
    while i <20:
        line = line.strip()
        L = []
        if L[0] == L[-1]:
            for letter in line:
                L.append(letter)
            print(L.reverse)
            i+=1
    
    