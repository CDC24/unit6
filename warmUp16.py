#Caleb Callaway
#5/11/18
#warmUp16.py - prints all file words that start with your first initial and ends with your last.

file=open("engmix.txt")


for stuff in file:
    line = stuff.strip()
    if len(line)>0 and line[0]=="c" and line[-1]=="c":
        print(line)