#Caleb Callaway
#5/21/18
#quiz6.py - quiz program

#Caleb Callaway
#5/21/18
#quiz6.py - quiz program

file = open ("engmix.txt")


                                    #Program 1

"""    
lett = input("what letter do you want? ")

for line in file:
    if (line.strip()).count(lett) == 4:
        print (line.strip())
"""

                                    #Program 2


for line in file:
    line = line.strip()
    if len(line) >= 9:
        if line[0] == line[4] and line[0] == line[8]:
            print (line)
            break
