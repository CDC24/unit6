#Caleb Callaway
#5/10/18
#howManyWords.py - print the number of words for each number of letters



file=open("engmix.txt").strip()



kindsawords=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for word in file:
            kindsawords[len(word)] += 1
            

print (kindsawords)
    
