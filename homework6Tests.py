#Caleb Callaway
#5/15/18
#homework6Tests.py - four homework programs


file=open("engmix.txt")



"""
word = input ("enter a word: ")

IN = False
for line in file:
    if line.strip() == word:
        print ("Yes!",word,"is in the dictionary!")
        IN = True
        break
if IN == False:
    print ("Oof!",word,"is NOT in the dictionary!")
"""

L = []
for line in file:
    L.append(line.strip())
    
num = int(input("Enter the number of the word you want: ))

print L[num+1]
    