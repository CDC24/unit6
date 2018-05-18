#Caleb Callaway
#5/17/18
#longShort.py - finds the longest and shortest word for each letter

file = open("engmix.txt")


T = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
longestWord = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
shortestWord = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

print ("longest:")
for i in range(0,25):
    for line in file:
        line = line.strip()
        if len(line)>0 and line[0] == T[i]:
            if len(line)> len(longestWord[i]):
                longestWord[i] = line
    print (longestWord[i])

print ("shortest (longer than 1 letter):")
for i in range(0,25):
    for line in file:
        line = line.strip()
        if len(line)>0 and line[0] == T[i]:
            if len(line)> len(longestWord[i]):
                longestWord[i] = line
    print (longestWord[i])