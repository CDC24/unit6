#Caleb Callaway
#5/11/18
#warmUp16.py - prints all file words that start with your first initial and ends with your last.

file=open("engmix.txt")


for line in file:
    if len(line)>=2:
        list = line.split()
        if list[0]=="c" and list[-1]=="c":
            print (line.strip())
    if len(line)<2:
        if "c" in line:
            print (line.strip())