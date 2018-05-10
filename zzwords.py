#Caleb Callaway
#5/10/18
#zzwords.py - print every word in dictionary with 'zz' in it



file=open("engmix.txt")

for word in file:
    if "zz" in word:
        print (word)
