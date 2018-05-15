#Caleb Callaway
#5/15/18
#homework6Tests.py - four homework programs


file=open("engmix.txt")

word = input ("enter a word: ")

IN = False
for line in file:
    if line.strip() == word:
        print ("Yes!",word,"is in the dictionary!")
        IN = True
        break
if IN == False:
    print ("Oof!",word,"is NOT in the dictionary!")
        