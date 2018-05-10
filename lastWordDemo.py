#Caleb Callaway
#5/10/18
#fileDemo.py - how to read a file



file=open("engmix.txt")


for line in file:
    if "cale" in line:
        print (line.strip())   #removes extra spaces from \n in original file
