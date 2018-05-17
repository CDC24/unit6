#Caleb Callaway
#5/17/18
#warmUp17.py- find all words in dictionary with letters of your name


file = open("engmix.txt")



for line in file:
    line = line.strip()
    if "c" in line:
        if "a" in line:
            if "l" in line:
                if "w" in line:
                    if "y" in line:
                        print (line)

print (" ")
print (" ")

for line in file:
    line = line.strip()
    if "c" in line:
        if "a" in line:
            if "l" in line:
                if "e" in line:
                    if "b" in line:
                        print (line)