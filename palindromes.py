#Caleb Callaway
#5/16/18
#palindromes.py - finds all the palindromes in the dictionary

file=open("engmix.txt")


for line in file:
    line = line.strip()
    reverse = ""
    for ch in line:
        reverse = ch+reverse
    if reverse == line:
        print (reverse)