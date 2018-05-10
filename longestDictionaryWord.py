#Caleb Callaway
#5/10/18
#longestDictionaryWord.py - print the longest word in the dictionary list

file=open("engmix.txt")

longest = ""

for word in file:
    if len(word) > len(longest):
        longest = word
print("The longest word is",longest)