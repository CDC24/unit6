#Caleb Callaway
#5/10/18
#howManyWords.py - print the number of words for each number of letters



file=open("engmix.txt")



kindsawords=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



for word in file:
    kindsawords[len(word.strip())-1] += 1
            

for i in range (0,21):
    print ("there are",kindsawords[i],"of",i,"- letter words.")
    
