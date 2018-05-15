#Caleb Callaway
#5/15/18
#homework6Tests.py - four homework programs


file=open("engmix.txt")


                #part 1
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

                #part 2
"""
L = []
for line in file:
    L.append(line.strip())
    
num = int(input("Enter the number of the word you want: "))

print (L[num-1])
"""

                #part 3
"""
file = open("warmUp16.py")

for line in file:
    print (line.strip(),"!")
"""

                #part 4

letter = input ("input the letter you want: ")
greatest = (0)
best = ("")


for line in file:
    line = line.strip()
    if letter in line:
        lettcount=0
        for letter in line:
            lettcount+=1
    if lettcount>greatest:
        greatest = lettcount
        best = line
print (best)










    