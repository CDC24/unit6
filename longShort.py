#Caleb Callaway
#5/17/18
#longShort.py - finds the longest and shortest word for each letter

file = open("engmix.txt")


T = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
longestWord = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]



for line in file:
    line = line.strip()
    if line[0] = "a":
        if len(line)> len(longestWord[0]):
            longestWord[0] = line
print (longestWord[0])