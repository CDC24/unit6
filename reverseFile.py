#Caleb Callaway
#5/10/18
#reverseFile.py - prints all file lines in reverse order


file=open(input("what file do you want to reverse? "))

Lines = []

for line in file:
    Lines.append(line.strip())

