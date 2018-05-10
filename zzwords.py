#Caleb Callaway
#5/10/18
#zzwords.py - print every word in dictionary with 'zz' in it
file=open("engmix.txt")

longest = ""

for word in file:
    if len(word) > len(longest):
        longest = word
print("The longest word is",longest)
