#Caleb Callaway
#5/17/18
#warmUp17.py- find all words in dictionary with letters of your name


file = open("engmix.py")



for line in file:
    line = line.strip()
    if "callaway" in line:
        print line
    