#Caleb Callaway
#5/15/18
#homework6Tests.py - four homework programs


file=open("engmix.txt")

word = input ("enter a word: ")

for line in file:
    if line.strip() == word:
        print ("Yes!",word,"is in the dictionary!")
        break
    else:
        print ("Oof!",word,"is NOT in the dictionary!")
        