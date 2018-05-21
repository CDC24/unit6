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

"""
for line in file:
    line = line.strip()
    if len(line) >= 9:
        if line[0] == line[4] and line[0] == line[8]:
            print (line)
            break
"""

                                    #Program 3

"""
num = int(input("Enter a number: "))
lett = input("Enter a letter: ")

for line in file:
    line = line.strip()
    if len(line) == num:
        if line[0] == lett:
            print (line)
"""



words = 0
for line in file:
    line = line.strip()
    if len(line) >= 10:
        words +=1
        if words == 8000:
            print (line)
            break

